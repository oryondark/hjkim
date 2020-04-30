package jsonparsertest;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Set;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class JsonParserTest {

	@SuppressWarnings("resource")
	public static void main(String[] args) throws FileNotFoundException, IOException, ParseException {
		
		//To split "\n" from json_file use for library BufferedReader
		BufferedReader buf = new BufferedReader(new FileReader("../ReviewsParser/sample/reviews_sample.txt"));
		
		String line = null;
		while((line = buf.readLine()) != null) {
			//
			JSONParser parser = new JSONParser();
			JSONObject obj = new JSONObject();
			obj = (JSONObject)parser.parse(line);
			
			@SuppressWarnings("rawtypes")
			Set keys = obj.keySet();

			System.out.println(keys);
			//for(int i = 0; i < key.length; i++) {
			//	System.out.println(key[i] + " " + obj.get(key[i]));
			//}
			
		}
		

	}

}
