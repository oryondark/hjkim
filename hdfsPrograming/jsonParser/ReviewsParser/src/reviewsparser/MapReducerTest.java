package reviewsparser;

import java.io.IOException;
import java.util.Set;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


public class MapReducerTest {
	
	
	//Map
	public static class ReviewerMap extends Mapper<LongWritable, Text, Text, Text>{
		//heap alloc
		public static Text getData;
		
		public void map(LongWritable key, Text jsonData, Context context ) throws IOException, InterruptedException {
			
			
			
			String toStr = jsonData.toString();
			Configure_Run.getData(toStr);
			
			String[] list = toStr.split("\n");
			Object[] key_list = null;
			
			
			//for(int i = 0; i < list.length; i++) {
				//
				JSONParser parser = new JSONParser();
				JSONObject obj = new JSONObject();
				
				try {
					obj = (JSONObject)parser.parse(list[0]);
					
					//get key list.
					if(key_list == null) {
						@SuppressWarnings("rawtypes")
						Set keys = obj.keySet();
						key_list = keys.toArray();
					}
					
					for(int i = 0; i < key_list.length; i++) {
						try {
						context.write(new Text((String) key_list[i]), new Text((String) obj.get(key_list[i])));
						} catch (Exception e) {
							continue;
						}
					}
					
				} catch (ParseException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
					
				}
				
				
			//}
		}
	}
	
	
	public static class ReviewerRed extends Reducer<Text, Text, Text, Text>{
		public void reduce(Iterable<Text> keys, Iterable<Text> value, Context context) throws IOException, NumberFormatException, InterruptedException{
			
			for(Text key : keys) {
				for(Text item : value) {
					context.write(key, item);
				}
			}
		}
	}
	

	
	
}
