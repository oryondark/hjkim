package mapreduce;

import java.util.*;

import java.io.IOException;
import java.lang.NumberFormatException;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

public class MapReducer {
	//Map
	public static class My_Map extends MapReduceBase implements
	Mapper<LongWritable, Text, Text, IntWritable>{
		public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException, NumberFormatException {
			
			String line = value.toString();
			String lasttoken = null;
			StringTokenizer s_token = new StringTokenizer(line, "\t");
			String year = s_token.nextToken();
			
			lasttoken = year;
			while(s_token.hasMoreTokens()) {
				lasttoken = s_token.nextToken();
			}
			
			int avgprice = Integer.parseInt(lasttoken);
			output.collect(new Text(year), new IntWritable(avgprice));
			
		}
		
		
	}
	
	
	public static class My_Reduce extends MapReduceBase implements
	Reducer<Text, IntWritable, Text, IntWritable>{
		public void reduce(Text key, Iterator <IntWritable> values, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException, NumberFormatException{
			
			int maxavg = 30;
			int val = Integer.MIN_VALUE;
			
			while(values.hasNext()) {
				val = values.next().get();
				if(val > maxavg) {
					output.collect(key, new IntWritable(val));
				}
			}
			
		}
		
	}
	
}
