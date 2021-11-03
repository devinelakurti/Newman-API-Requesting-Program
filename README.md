----------------------
How to install Newman:
----------------------

If you have npm installed, run this command in your command-line interface (CLI) "npm install -g newman"

If you don’t have npm installed,

Download and install Node.js.
Then, run the command "npm install -g newman" in your CLI.


----------------------
Command Line Arguments
----------------------
newman run <postman collection json file name> -d <input file name > --delay-request <how much delay between the requests> >> <output file>

Example commmand:
newman run DNATest.postman_collection_Ensembl.json -d "test.csv" --delay-request 10 >> testfinal.out


-------------------------
Issues
-------------------------

Q.  File not found error postman collection json file , input file and  output? 

A.  Better to keep all these files in the same directory to avoid this issue. 
    
Q.  How to keep the input files "postman collection json file , input file and  output"? 

A.  In case if you want to keep input files in different directories then refer them with full path or absolute path
	
e.g  if you keep all the input files in the directory "D:\testing\" then you should refer those input files as below
![image](https://user-images.githubusercontent.com/35899476/140198736-7063effd-17fc-483b-9e38-47edb4572773.png)
