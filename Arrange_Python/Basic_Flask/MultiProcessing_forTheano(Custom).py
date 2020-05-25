from multiprocessing import Pool
from werkzeug.exceptions import HTTPException
from flask import Flask, flash, request, redirect, url_for
import sys
import cv2 as cv
import pickle
from endToendMachine_Theano import * # Custom Theano tools.

app = Flask('test')
uploaded_folder = 'uploaded/'
extensions = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = uploaded_folder

#_pool = None
dl_model = pickle.load(open('theano_model.pkl','rb'))
knn_model = pickle.load(open('knn_model.pkl', 'rb'))

def multi_server_pool(name, port):
    app.run('0.0.0.0', port, threaded=True)


def image_decoder(baseImg):
    #image_decode_time = time.time()
    x = base64.b64decode(baseImg) # base64 to bytes
    return x

def theano_predict(img_path):
    target_im = cv.imread(img_path, cv.IMREAD_COLOR)
    if (target_im.shape[0] > 100) and(target_im.shape[1] > 100):
        target_im = cm.cropManager(img_path, target_im)
        target_im.square_crop(64)
        target_im = target_im.cut_save_image()

    target_im = cv.resize(target_im, (64, 64), interpolation = cv.INTER_AREA)
    target_im = target_im.astype(np.float32)
    cv.normalize(target_im, target_im, 0, 1, cv.NORM_MINMAX)
    target_im = np.transpose(target_im, (2,0,1))
    ret = predict(target_im)
    return ret

@app.route('/', methods=['PUT'])
def hello():
    global sum
    sum = 0
    recv_file = request.files['data']
    #print(recv_file.filename)
    abs_path_for = os.path.join(app.config['UPLOAD_FOLDER'], recv_file.filename)
    #print(abs_path_for)
    recv_file.save(abs_path_for)
    result_inf = _pool.apply_async(theano_predict, [abs_path_for])
    res = result_inf.get()
    return res


@app.errorhandler(Exception)
def bad_req_handler(e):
    recv_file = request.files['data']
    abs_path_for = os.path.join(app.config['UPLOAD_FOLDER'], recv_file.filename)
    result_inf = _pool.apply_async(theano_predict, [abs_path_for])
    res = result_inf.get()

    return res

'''
Multiprocessing Flask
'''
if __name__ == '__main__':
    _pool = Pool(processes=2) # just using 2 processor
    try:
        app.run('0.0.0.0', sys.argv[1], threaded=True)

    except KeyboardInterrupt:
        _pool.close()
        _pool.join()
