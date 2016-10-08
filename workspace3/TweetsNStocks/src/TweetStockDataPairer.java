import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;

public class TweetStockDataPairer {
	public static void createPair(String StockFile, String DescriptorFile, String XValFile) throws IOException {
		Map<String, String> stockupdown = new HashMap<String, String>();
		CSVReader StockReader = new CSVReader(new FileReader(StockFile), '\t');
		CSVWriter XValWriter = new CSVWriter(new FileWriter(XValFile));
		StockReader.readNext();
		String[] readLine;
		while ((readLine = StockReader.readNext()) != null) {
			stockupdown.put(readLine[1], readLine[readLine.length - 2]);
		}
		String writeLine[];
		StockReader.close();
		CSVReader DescriptorReader = new CSVReader(new FileReader(DescriptorFile));
		readLine = DescriptorReader.readNext();
		writeLine = new String[readLine.length + 1];
		for (int i = 0; i < readLine.length; i++) {
			writeLine[i] = readLine[i];
		}
		writeLine[readLine.length] = "+/-/=";
		XValWriter.writeNext(writeLine);
		while ((readLine = DescriptorReader.readNext()) != null) {

			if (stockupdown.containsKey(readLine[0])) {
				for (int i = 0; i < readLine.length; i++) {
					writeLine[i] = readLine[i];
				}
				writeLine[readLine.length] = stockupdown.get(readLine[0]);
				XValWriter.writeNext(writeLine);
			}

		}

		DescriptorReader.close();
	}

	public static void createPairsFolders(String DescriptorFolder, String StockFolder, String XValOutputFolder) {
		for (File DescriptorFile : new File(DescriptorFolder).listFiles()) {
			try {
				createPair(DescriptorFile.getPath(), StockFolder + "/"
						+ DescriptorFile.getName().substring(0, DescriptorFile.getName().indexOf(".")) + "_cleaned.csv",
						XValOutputFolder);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

	public static void main(String[] args) {
createPairsFolders("../../descriptors","../../stock_data/tweet_date_data","../../XValSets");
	}
}
