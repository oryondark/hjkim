def get_all_dataset():
    all_dataset = []
    root = "Root Directory"
    for cls in os.listdir(root):
        path_to_class = os.path.join(root,cls)
        for item in os.listdir(path_to_class):
            img = cv.imread(os.path.join(path_to_class, item))
            img = cv.resize(img, (64, 64), interpolation = cv.INTER_AREA)
            img = img.astype(np.float32)
            cv.normalize(img, img, 0, 1, cv.NORM_MINMAX)

            img = np.transpose(img, [2,0,1])
            img = torch.Tensor(img)

            _, _, conv1 = model(torch.unsqueeze(img,0).cuda())
            conv1 = conv1.cpu().detach().numpy().squeeze(0)

            reshape = []
            for i in range(0,len(conv1)):
                reshape.append(conv1[i].flatten())


            all_dataset.append(reshape)

    return all_dataset
