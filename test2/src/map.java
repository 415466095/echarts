//import org.springframework.web.servlet.mvc.Controller;
//import org.springframework.web.servlet.ModelAndView;
//import javax.servlet.http.HttpServletRequest;
//import javax.servlet.http.HttpServletResponse;
import java.io.*;
import java.util.*;

class HandleCsv {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(
                        new FileInputStream("/home/hadoop/文档/JAVA可视化/Steam_games.csv")
                )
        );


        String line;
        String name;
        String age;
        String birthday;
        while ( (line = br.readLine()) != null ) {
            //System.out.println(line);
            String[] info = line.split(",");
            name = info[0].trim();
            age = info[1].trim();
            birthday = info[2].trim();

         //  System.out.println(getType(name));
          if(birthday!="0") {
              System.out.print(name + "\t" + age + "\t" + birthday + "\n");
          }
        }
    }
    public static String getType(Object o){ //获取变量类型方法

        return o.getClass().toString(); //使用int类型的getClass()方法

    }

}

