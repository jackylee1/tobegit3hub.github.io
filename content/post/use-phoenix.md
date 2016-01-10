+++
date = "2013-11-28T08:35:30+08:00"
draft = true
title = "use phoenix"

+++



<pre><code>
package cn.chendihao.java;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.Statement;

public class MainClass {

  public static void main(String[] args) throws SQLException {

    long startTime = System.currentTimeMillis();

    Statement stmt = null;
    ResultSet rset = null;

    Connection con = DriverManager.getConnection("jdbc:phoenix:localhost");
    // stmt = con.createStatement();                                                                                                                                                                                
    //                                                                                                                                                                                                              
    // stmt.executeUpdate("create table test2 (mykey integer not null primary key, mycolumn varchar)");                                                                                                             
    // stmt.executeUpdate("upsert into test values (1,'Hello2')");                                                                                                                                                  
    // stmt.executeUpdate("upsert into test values (2,'World2!')");                                                                                                                                                 
    // con.commit();                                                                                                                                                                                                

    // PreparedStatement statement = con.prepareStatement("select * from test");                                                                                                                                    
    PreparedStatement statement = con.prepareStatement("select count(*) from PHOENIX_ROWCOUNT");
    rset = statement.executeQuery();
    while (rset.next()) {
      // System.out.println(rset.getString("mycolumn"));                                                                                                                                                            
      System.out.println(rset.getInt(1));
    }
    statement.close();
    con.close();

    long endTime = System.currentTimeMillis();

    System.out.println("Total time = " + (endTime - startTime) / 1000 + " seconds!!!");

  }
}
</code></pre>