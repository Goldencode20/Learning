package HueAndCues;

import java.io.File;
import java.io.FileInputStream;
import java.util.Iterator;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;

public class HintGiver {
    
    String[][] oneWord, twoWord;

    public void importGuesses() {
        try {
            FileInputStream file = new FileInputStream("Guess.xlsx");
            XSSFWorkbook workbook = new XSSFWorkbook(file);
            XSSFSheet sheet1 = workbook.getSheetAt(0);
            XSSFSheet sheet2 = workbook.getSheetAt(1);
            int rows = sheet1.getPhysicalNumberOfRows();
            int cells = sheet1.getRow(sheet1).getPhysicalNumberOfCells();
            oneWord = new String[rows][cells];
            twoWord = new String[rows][cells];
            for(int r = 0; r < rows; r++) {
                XSSFRWow row = sheet1.getRow(r);
                XSSFRWow row1 = sheet2.getRow(r);
                if (row != null) {
                    for (int c = 0; c < cells; c++) {
                        XSSFCell cell = row.getCell(c);
                        XSSFCell cell1 = row1.getCell(c);
                        oneWord[r][c] = cell.getStringCellValue();
                        twoWord[r][c] = cell1.getStringCellValue();
                    }
                }

            }

            file.close();
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }

    public static void main( String args[]) {
        
    }
}
