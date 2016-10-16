import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class DeleteDuplicates {
	public static void deleteDuplicatesByFolders(String TweetsFolder,String outputFolder){
File[] TweetFolderArray = new File(TweetsFolder).listFiles();
for(File compFolder: TweetFolderArray){
	for(File DayTweet: compFolder.listFiles()){
		try {
			File outputCompFolder =  new File(outputFolder+"/"+compFolder.getName());
			if(!outputCompFolder.exists())
				outputCompFolder.mkdir();
			deleteDuplicatesFile(DayTweet.getPath(),outputFolder+"/"+compFolder.getName()+"/"+DayTweet.getName());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

	}
	
	public static void deleteDuplicatesFile(String inputfile,String outputFile) throws IOException{
		BufferedReader bR= new BufferedReader(new FileReader(inputfile));
		BufferedWriter bW = new BufferedWriter(new FileWriter(outputFile));
		ArrayList<String> noURLTweets = new ArrayList<String>();
		String readLine;
		while((readLine=bR.readLine())!=null){
		//	System.out.println("readLine= " +readLine);
			if (!noURLTweets.contains(removeUrl(readLine))){
				noURLTweets.add(removeUrl(readLine));
				bW.write(removeUrl(readLine)+"\r\n");
			}
		}
		bR.close();
		bW.close();
		
	}
	
	
	private static String removeUrl(String commentstr)
    {
		
		return commentstr.replaceAll("https?://\\S+\\s?", "");
    }
	
	public static void main(String[] args){
		deleteDuplicatesByFolders("../../AllTweets/Tweets","../../AllTweets/noDupliTweets");
	}
	
}