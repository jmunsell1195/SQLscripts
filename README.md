# SQLscripts

This python script was written to extract tables from a postgre-sql database attatched to an educational web application built to teach students principles of physics.

The script uses the psycopg2 library to do the following things
<ul>
  <li>
    Connects to the database
  </li>
  <li>
     Makes a list of all the tables with "Force" in the name
  </li>
  <li>
    Grabs the column names for each table
  </li>
  <li>
    Grabs the row data
  </li>
  <li>
     Uses os.mkdir() to make a new directory
  </li>
  <li>
     Uses csv.writer() to write a .csv in the new directory
  </li>
</ul>
