////// GENRE

// CATEGORY
CREATE (:Category { genre: "Fantasy"}), 
(:Category { genre: "Adventure"}), 
(:Category { genre: "Romance"}), 
(:Category { genre: "Contemporary"}), 
(:Category { genre: "Dystopian"}), 
(:Category { genre: "Mystery"}), 
(:Category { genre: "Horror"}), 
(:Category { genre: "Thriller"}), 
(:Category { genre: "Paranormal"}), 
(:Category { genre: "Historical fiction"}), 
(:Category { genre: "Science Fiction"}), 
(:Category { genre: "Memoir"}), 
(:Category { genre: "Cooking"}), 
(:Category { genre: "Art"}), 
(:Category { genre: "Self-help / Personal"}), 
(:Category { genre: "Development"}), 
(:Category { genre: "Motivational"}), 
(:Category { genre: "Health"}), 
(:Category { genre: "History"}), 
(:Category { genre: "Travel"}), 
(:Category { genre: "Guide / How-to"}), 
(:Category { genre: " Families & Relationships"}), 
(:Category { genre: "Humor"}), 
(:Category { genre: "Children’s"})


////// LOCATION

// WING
CREATE (:Wing {floor:"G",wing: "East Wing", rep:"GEW"}),
(:Wing {floor:"G", wing: "West Wing", rep:"GWW"}),
(:Wing {floor:"G", wing: "North Wing", rep:"GNW"}),
(:Wing {floor:"G", wing: "South Wing", rep:"GSW"}),
(:Wing {floor:"G", wing: "Far-East Wing", rep:"GFEW"}),
(:Wing {floor:"1st",wing: "First East Wing", rep:"FEW"}),
(:Wing {floor:"1st", wing: "First West Wing", rep:"FWW"}),
(:Wing {floor:"1st",wing: "First Far-East Wing", rep:"FFEW"}),
(:Wing {floor:"2nd",wing: "Second Far-East Wing", rep:"SFEW"})

// FLOOR
CREATE (:Floor {floor: "Ground", rep: "G", building: "Block-2"}),
(:Floor {floor: "First", rep: "1st", building: "Block-2"}),
(:Floor {floor: "Second", rep: "2nd", building: "Block-2"})


////// PERSON

// STAFF
CREATE (:Staff {Name: "Amethyst Macias",Email: "eros@vulputaterisusa.co.uk",City: "Gorkha",Phone: "+977-987-4941154"}), 
(:Staff {Name: "Walker Vinson",Email: "condimentum.eget@aceleifend.co.uk",City: "Dolakha",Phone: "+977-988-3286995"}), 
(:Staff {Name: "Allen Higgins",Email: "purus.Nullam@Mauriseuturpis.net",City: "Syangja",Phone: "+977-981-8521520"}), 
(:Staff {Name: "Abbot Page",Email: "metus.In@Nulla.net",City: "Lalitpur",Phone: "+977-981-8220261"}), 
(:Staff {Name: "Yardley Morris",Email: "tempor@vehicula.edu",City: "Parsa",Phone: "+977-980-7144013"}), 
(:Staff {Name: "Cullen Campos",Email: "tristique.ac@erat.edu",City: "Parsa",Phone: "+977-980-7245428"}), 
(:Staff {Name: "Ina Terry",Email: "nunc.sed.pede@non.org",City: "Kapilvastu",Phone: "+977-989-2044529"}), 
(:Staff {Name: "Adara Parks",Email: "venenatis.vel@Innecorci.co.uk",City: "Kapilvastu",Phone: "+977-985-9980400"}), 
(:Staff {Name: "Hop Campos",Email: "ornare.In.faucibus@etcommodo.edu",City: "Morang",Phone: "+977-980-6461829"}), 
(:Staff {Name: "Aphrodite Glover",Email: "neque.vitae.semper@faucibusorciluctus.edu",City: "Parsa",Phone: "+977-985-5596137"}), 
(:Staff {Name: "Roary Contreras",Email: "non@Phasellusdolor.ca",City: "Chitwan",Phone: "+977-981-6212198"}), 
(:Staff {Name: "Alana Merrill",Email: "lorem@cubiliaCurae.com",City: "Panauti",Phone: "+977-987-5832198"}), 
(:Staff {Name: "Baker Tillman",Email: "vitae.erat@semper.com",City: "Sarlahi",Phone: "+977-989-6245901"}), 
(:Staff {Name: "Jeanette Guthrie",Email: "blandit@dictum.edu",City: "Jhapa",Phone: "+977-980-9757454"}), 
(:Staff {Name: "Leigh Ortega",Email: "adipiscing.elit.Etiam@faucibusMorbivehicula.net",City: "Saptari",Phone: "+977-984-6196459"}), 
(:Staff {Name: "Cyrus Kim",Email: "pellentesque.Sed.dictum@egestas.edu",City: "Bhojpur",Phone: "+977-982-6009630"}), 
(:Staff {Name: "Ila Crosby",Email: "Fusce@magnisdis.co.uk",City: "Palpa",Phone: "+977-981-1832167"}), 
(:Staff {Name: "Rylee Macias",Email: "dolor@odio.org",City: "Sarlahi",Phone: "+977-985-1364335"}), 
(:Staff {Name: "Natalie Atkinson",Email: "eget.metus.In@semperrutrumFusce.org",City: "Lalitpur",Phone: "+977-981-1421479"}), 
(:Staff {Name: "Montana Wiley",Email: "blandit@tempus.co.uk",City: "Sarlahi",Phone: "+977-983-8266218"}), 
(:Staff {Name: "Maile Hopper",Email: "eget.odio@sedleo.org",City: "Lalitpur",Phone: "+977-982-5213748"}), 
(:Staff {Name: "Galvin Morgan",Email: "orci.lobortis.augue@egetvariusultrices.org",City: "Saptari",Phone: "+977-984-7171362"}), 
(:Staff {Name: "Riley Jacobs",Email: "nulla.Integer@Nullamsuscipitest.edu",City: "Kathmandu",Phone: "+977-987-5261996"}), 
(:Staff {Name: "Aquila Hughes",Email: "Nullam@urnaUttincidunt.org",City: "Jhapa",Phone: "+977-981-5376013"}), 
(:Staff {Name: "Deirdre Macias",Email: "nascetur.ridiculus.mus@ametrisusDonec.net",City: "Dolakha",Phone: "+977-987-4136190"}), 
(:Staff {Name: "Kasper Maxwell",Email: "Nulla.dignissim@Etiam.co.uk",City: "Lalitpur",Phone: "+977-988-9079365"}), 
(:Staff {Name: "Camille Roman",Email: "tellus.Suspendisse.sed@dignissimMaecenasornare.com",City: "Kathmandu",Phone: "+977-982-7314846"}), 
(:Staff {Name: "Clayton Castillo",Email: "in@eu.net",City: "Morang",Phone: "+977-986-3036185"}), 
(:Staff {Name: "Noel Odonnell",Email: "ac.feugiat@imperdieterat.org",City: "Kapilvastu",Phone: "+977-984-7065026"}), 
(:Staff {Name: "Signe Baldwin",Email: "sit@Nuncsed.org",City: "Bhojpur",Phone: "+977-989-7749888"})


// STUDENT 
CREATE (:Student {Name: "Brandon Wiley",Email: "Proin.dolor.Nulla@Pellentesque.co.uk",City: "Syangja",Phone: "+977-988-2148696"}), 
(:Student {Name: "Sylvester Jackson",Email: "parturient.montes@ipsumcursus.com",City: "Panauti",Phone: "+977-982-3559785"}), 
(:Student {Name: "Lysandra Bell",Email: "mi.Aliquam.gravida@Quisqueimperdiet.org",City: "Morang",Phone: "+977-985-4177862"}), 
(:Student {Name: "Ashely Pittman",Email: "elit@Loremipsum.edu",City: "Palpa",Phone: "+977-987-1461326"}), 
(:Student {Name: "Vaughan Barnes",Email: "eget.magna@etnunc.com",City: "Sarlahi",Phone: "+977-982-6432675"}), 
(:Student {Name: "Serina Delgado",Email: "ligula.Aenean@ametante.co.uk",City: "Panauti",Phone: "+977-988-1575390"}), 
(:Student {Name: "Gisela Mcfarland",Email: "mauris@Fusce.ca",City: "Saptari",Phone: "+977-984-5846654"}), 
(:Student {Name: "Keegan Melton",Email: "lobortis@tellusPhasellus.ca",City: "Morang",Phone: "+977-985-5103388"}), 
(:Student {Name: "Alana White",Email: "ligula@ametconsectetueradipiscing.net",City: "Syangja",Phone: "+977-985-4301869"}), 
(:Student {Name: "Rudyard Bradley",Email: "elementum@pharetranibhAliquam.net",City: "Parsa",Phone: "+977-981-9878743"}), 
(:Student {Name: "Macaulay Foster",Email: "dapibus@velitSedmalesuada.ca",City: "Dolakha",Phone: "+977-983-9105986"}), 
(:Student {Name: "Isabella Frank",Email: "ipsum.Curabitur@faucibusorci.org",City: "Dolakha",Phone: "+977-986-7115499"}), 
(:Student {Name: "Castor Terry",Email: "sem.Pellentesque@Proinvelarcu.com",City: "Morang",Phone: "+977-985-7589739"}), 
(:Student {Name: "Kaden Mueller",Email: "facilisi@Integer.edu",City: "Bhojpur",Phone: "+977-986-9588922"}), 
(:Student {Name: "Halee Barron",Email: "semper.rutrum.Fusce@ut.ca",City: "Kapilvastu",Phone: "+977-986-4996995"}), 
(:Student {Name: "Zeus Coffey",Email: "lectus@dictumultricies.com",City: "Jhapa",Phone: "+977-982-6497072"}), 
(:Student {Name: "Ella Stone",Email: "neque.pellentesque.massa@tellus.net",City: "Kapilvastu",Phone: "+977-982-3590113"}), 
(:Student {Name: "Ainsley Puckett",Email: "lorem.fringilla@feugiatSed.co.uk",City: "Lalitpur",Phone: "+977-985-6610711"}), 
(:Student {Name: "Amery Walker",Email: "tempus.eu@consequatlectussit.org",City: "Panauti",Phone: "+977-986-1741946"}), 
(:Student {Name: "Garrison Richard",Email: "Donec@est.co.uk",City: "Syangja",Phone: "+977-989-8307617"}), 
(:Student {Name: "Rinah Mosley",Email: "lorem.auctor@liberoMorbi.net",City: "Dolakha",Phone: "+977-985-1487653"}), 
(:Student {Name: "Dorothy Bryan",Email: "sit.amet@velitdui.ca",City: "Palpa",Phone: "+977-982-3885716"}), 
(:Student {Name: "Miriam Hopper",Email: "fringilla@in.ca",City: "Bhojpur",Phone: "+977-983-7013352"}), 
(:Student {Name: "Kane Cash",Email: "malesuada.id.erat@adipiscingMauris.co.uk",City: "Dolakha",Phone: "+977-987-5584339"}), 
(:Student {Name: "Ainsley Guy",Email: "in.consectetuer.ipsum@turpisegestasFusce.com",City: "Parsa",Phone: "+977-982-7745396"}), 
(:Student {Name: "Mariam Gallegos",Email: "at.arcu.Vestibulum@tellusjustosit.net",City: "Gorkha",Phone: "+977-986-7388111"}), 
(:Student {Name: "Karen Lyons",Email: "dignissim@risusquis.net",City: "Morang",Phone: "+977-981-1686655"}), 
(:Student {Name: "Hannah Mclean",Email: "non@egetvenenatisa.co.uk",City: "Parsa",Phone: "+977-985-6917498"}), 
(:Student {Name: "Karleigh Ballard",Email: "ac.urna.Ut@accumsanconvallisante.org",City: "Kapilvastu",Phone: "+977-986-9669429"}), 
(:Student {Name: "Ira Bennett",Email: "adipiscing.enim@Proinvelarcu.net",City: "Kapilvastu",Phone: "+977-981-6382479"}), 
(:Student {Name: "Melissa Conrad",Email: "rhoncus.Donec.est@Namporttitor.com",City: "Gorkha",Phone: "+977-984-7605700"}), 
(:Student {Name: "Kristen Underwood",Email: "malesuada.vel.venenatis@antebibendum.net",City: "Syangja",Phone: "+977-982-6616606"}), 
(:Student {Name: "Regina Ball",Email: "non@tellusnonmagna.org",City: "Parsa",Phone: "+977-983-8071806"}), 
(:Student {Name: "Marvin Rojas",Email: "imperdiet.nec.leo@sedsapienNunc.org",City: "Sarlahi",Phone: "+977-982-8456501"}), 
(:Student {Name: "Ashely Morris",Email: "iaculis.nec@atvelitCras.org",City: "Parsa",Phone: "+977-980-4877833"}), 
(:Student {Name: "Bernard Whitehead",Email: "scelerisque.lorem.ipsum@metus.net",City: "Kapilvastu",Phone: "+977-982-9635410"}), 
(:Student {Name: "Lara Doyle",Email: "risus.Donec.nibh@egestasurna.edu",City: "Palpa",Phone: "+977-982-4919852"}), 
(:Student {Name: "Amethyst Whitney",Email: "Proin.dolor.Nulla@ipsumSuspendisse.co.uk",City: "Bhaktapur",Phone: "+977-983-9628758"}), 
(:Student {Name: "Moana Elliott",Email: "justo.faucibus.lectus@urnaNullamlobortis.ca",City: "Syangja",Phone: "+977-986-2949279"}), 
(:Student {Name: "Sloane Bender",Email: "nunc.sed@quisdiam.edu",City: "Bhojpur",Phone: "+977-987-8685559"}), 
(:Student {Name: "Jescie Rivers",Email: "malesuada.fames@ascelerisque.co.uk",City: "Bhojpur",Phone: "+977-985-5551245"}), 
(:Student {Name: "Beau Whitney",Email: "fringilla.mi.lacinia@sedfacilisisvitae.net",City: "Bhojpur",Phone: "+977-981-6142221"}), 
(:Student {Name: "Paula Dyer",Email: "Duis@gravidaAliquamtincidunt.org",City: "Morang",Phone: "+977-985-6538181"}), 
(:Student {Name: "Piper Herring",Email: "congue.In.scelerisque@auctornuncnulla.co.uk",City: "Syangja",Phone: "+977-989-6133997"}), 
(:Student {Name: "Inez Orr",Email: "in@enimgravida.org",City: "Panauti",Phone: "+977-982-3489101"}), 
(:Student {Name: "Nita Black",Email: "risus@urnaUt.com",City: "Parsa",Phone: "+977-984-9835131"}), 
(:Student {Name: "Lynn Franks",Email: "tincidunt@Ut.co.uk",City: "Gorkha",Phone: "+977-983-4221360"}), 
(:Student {Name: "Xanthus Lott",Email: "ridiculus.mus.Donec@In.org",City: "Jhapa",Phone: "+977-983-7870039"}), 
(:Student {Name: "Kato Kent",Email: "nisi.sem@Nullamnisl.com",City: "Chitwan",Phone: "+977-982-3964466"}), 
(:Student {Name: "Zane Richmond",Email: "nisi.a@per.net",City: "Kathmandu",Phone: "+977-982-7990950"}), 
(:Student {Name: "Kuame Vincent",Email: "aliquet.molestie@Nullaegetmetus.co.uk",City: "Panauti",Phone: "+977-982-9130608"}), 
(:Student {Name: "Stuart Randall",Email: "neque@Craseu.co.uk",City: "Dolakha",Phone: "+977-982-3002991"}), 
(:Student {Name: "Elvis Glover",Email: "imperdiet@sitametconsectetuer.com",City: "Kathmandu",Phone: "+977-980-5365391"}), 
(:Student {Name: "Cyrus Bean",Email: "neque@ridiculusmusDonec.co.uk",City: "Kapilvastu",Phone: "+977-982-8569940"}), 
(:Student {Name: "Chiquita Dominguez",Email: "ut@Suspendisse.net",City: "Syangja",Phone: "+977-986-8804003"}), 
(:Student {Name: "Gage Clay",Email: "porttitor.scelerisque.neque@ligulaDonecluctus.org",City: "Lalitpur",Phone: "+977-983-8972589"}), 
(:Student {Name: "Cade Patrick",Email: "mauris@Phasellusinfelis.ca",City: "Gorkha",Phone: "+977-987-1649218"}), 
(:Student {Name: "Stephanie Moody",Email: "dignissim@elementumategestas.ca",City: "Bhaktapur",Phone: "+977-989-1867027"}), 
(:Student {Name: "Jin Adams",Email: "magna.malesuada@ultriciessemmagna.edu",City: "Lalitpur",Phone: "+977-989-9154819"}), 
(:Student {Name: "Beverly Paul",Email: "Sed.pharetra.felis@fermentumrisusat.edu",City: "Syangja",Phone: "+977-984-2761295"}), 
(:Student {Name: "Liberty Huff",Email: "arcu@hendrerita.ca",City: "Saptari",Phone: "+977-986-4342117"}), 
(:Student {Name: "Willa Ayala",Email: "eu.elit.Nulla@rhoncus.ca",City: "Bhojpur",Phone: "+977-989-6501390"}), 
(:Student {Name: "Quentin Sharpe",Email: "quam.Curabitur@InfaucibusMorbi.net",City: "Dolakha",Phone: "+977-985-5810138"}), 
(:Student {Name: "Zahir Cantu",Email: "venenatis.lacus.Etiam@mattisvelit.com",City: "Bhaktapur",Phone: "+977-986-8315793"}), 
(:Student {Name: "Bevis Mcfadden",Email: "Phasellus.nulla.Integer@nisidictum.co.uk",City: "Gorkha",Phone: "+977-981-3551329"}), 
(:Student {Name: "Holly Everett",Email: "penatibus.et.magnis@quisaccumsanconvallis.net",City: "Syangja",Phone: "+977-986-1375888"}), 
(:Student {Name: "Karyn Goodman",Email: "Maecenas.ornare.egestas@esttempor.edu",City: "Bhaktapur",Phone: "+977-981-7204432"}), 
(:Student {Name: "Sonia Mccormick",Email: "leo@metusurnaconvallis.org",City: "Sarlahi",Phone: "+977-983-9402120"}), 
(:Student {Name: "Shafira Burke",Email: "amet@consectetueradipiscingelit.co.uk",City: "Palpa",Phone: "+977-986-5730439"}), 
(:Student {Name: "Amaya May",Email: "pede.Cras.vulputate@utlacusNulla.co.uk",City: "Bhojpur",Phone: "+977-981-5741917"})  

// OCCUPATION
CREATE (:Occupation {role: "Teacher"}),
(:Occupation {role: "Librarian"}),
(:Occupation {role: "Security Guard"}),
(:Occupation {role: "Resource Manager"})

// DEPARTMENT
CREATE (:Department {Name:"Computer"}),
(:Department {Name:"Mechanical"}),
(:Department {Name:"Electrical"}),
(:Department {Name:"Mathematics"}),
(:Department {Name:"Physics"}),
(:Department {Name:"Chemistry"}),
(:Department {Name:"Civil"}),
(:Department {Name:"Biology"})

//SCHOOL
CREATE (:School {Name: "School of Science", ref:"SoS"}),
(:School {Name: "School of Enginerring", ref:"SoE"})


///// RELATIONSHIPS

// # RELATIONSHIPS

MATCH (G:Floor {rep:"G"})
MATCH (F:Floor {rep:"1st"})
MATCH (S:Floor {rep:"2nd"})

MATCH (GW:Wing {floor:"G"})
MATCH (FW:Wing {floor:"1st"})
MATCH (SW:Wing {floor:"2nd"})

MERGE (G)-[:HAS_WING]->(GW)
MERGE (F)-[:HAS_WING]->(FW)
MERGE (S)-[:HAS_WING]->(SW)


// # STAFF
MATCH (a:Staff {Name: "Amethyst Macias"}) 
MATCH (b:Staff {Name: "Walker Vinson"})
MATCH (c:Staff {Name: "Allen Higgins"})
MATCH (d:Staff {Name: "Abbot Page"})
MATCH (e:Staff {Name: "Yardley Morris"})
MATCH (f:Staff {Name: "Cullen Campos"})
MATCH (g:Staff {Name: "Ina Terry"})
MATCH (h:Staff {Name: "Adara Parks"})
MATCH (i:Staff {Name: "Hop Campos"})
MATCH (j:Staff {Name: "Aphrodite Glover"})
MATCH (k:Staff {Name: "Roary Contreras"})
MATCH (l:Staff {Name: "Alana Merrill"})
MATCH (m:Staff {Name: "Baker Tillman"})
MATCH (n:Staff {Name: "Jeanette Guthrie"})
MATCH (o:Staff {Name: "Leigh Ortega"})
MATCH (p:Staff {Name: "Cyrus Kim"})
MATCH (q:Staff {Name: "Ila Crosby"})
MATCH (r:Staff {Name: "Rylee Macias"})
MATCH (s:Staff {Name: "Natalie Atkinson"})
MATCH (t:Staff {Name: "Montana Wiley"})
MATCH (u:Staff {Name: "Maile Hopper"})
MATCH (v:Staff {Name: "Galvin Morgan"})
MATCH (w:Staff {Name: "Riley Jacobs"})
MATCH (x:Staff {Name: "Aquila Hughes"})
MATCH (y:Staff {Name: "Deirdre Macias"})
MATCH (z:Staff {Name: "Kasper Maxwell"})
MATCH (aa:Staff {Name: "Camille Roman"})
MATCH (ab:Staff {Name: "Clayton Castillo"})
MATCH (ac:Staff {Name: "Noel Odonnell"})
MATCH (ad:Staff {Name: "Signe Baldwin"})

MATCH (z1:Occupation {role: "Teacher"})
MATCH (z2:Occupation {role: "Librarian"})
MATCH (z3:Occupation {role: "Security Guard"})
MATCH (z4:Occupation {role: "Resource Manager"})

MERGE (z1)<-[:WORKS_AS]-(a)
MERGE (z1)<-[:WORKS_AS]-(b)
MERGE (z1)<-[:WORKS_AS]-(c)
MERGE (z1)<-[:WORKS_AS]-(d)
MERGE (z1)<-[:WORKS_AS]-(e)
MERGE (z1)<-[:WORKS_AS]-(f)
MERGE (z1)<-[:WORKS_AS]-(g)
MERGE (z1)<-[:WORKS_AS]-(h)
MERGE (z1)<-[:WORKS_AS]-(i)
MERGE (z1)<-[:WORKS_AS]-(j)
MERGE (z1)<-[:WORKS_AS]-(k)
MERGE (z1)<-[:WORKS_AS]-(l)
MERGE (z1)<-[:WORKS_AS]-(m)MATCH (n:Department) where n.Name= "Computer" OR n.Name= "Mechanical" OR n.Name= "Electrical" OR n.Name= "Civil"  
MATCH (s:School {ref:"SoE"})
MERGE (n)-[:DEPARTMENT_OF]->(s)

MATCH (n:Department) where NOT IN (n.Name= "Computer" AND n.Name= "Mechanical" AND n.Name= "Electrical" AND n.Name= "Civil") 
MERGE (z1)<-[:WORKS_AS]-(n)
MERGE (z1)<-[:WORKS_AS]-(o)

MERGE (z2)<-[:WORKS_AS]-(p)
MERGE (z2)<-[:WORKS_AS]-(q)
MERGE (z2)<-[:WORKS_AS]-(r)
MERGE (z2)<-[:WORKS_AS]-(s)
MERGE (z2)<-[:WORKS_AS]-(t)

MERGE (z3)<-[:WORKS_AS]-(u)
MERGE (z3)<-[:WORKS_AS]-(v)
MERGE (z3)<-[:WORKS_AS]-(w)
MERGE (z3)<-[:WORKS_AS]-(x)
MERGE (z3)<-[:WORKS_AS]-(y)

MERGE (z4)<-[:WORKS_AS]-(z)
MERGE (z4)<-[:WORKS_AS]-(aa)
MERGE (z4)<-[:WORKS_AS]-(ab)
MERGE (z4)<-[:WORKS_AS]-(ac)
MERGE (z4)<-[:WORKS_AS]-(ad)


// #LOCATION

MATCH (gew:Wing { rep:"GEW"})
MATCH (gww:Wing { rep:"GWW"})
MATCH (gnw:Wing { rep:"GNW"})
MATCH (gsw:Wing { rep:"GSW"})
MATCH (gfew:Wing { rep:"GFEW"})

MATCH (few:Wing {rep:"FEW"})
MATCH (fww:Wing {rep:"FWW"})
MATCH (ffew:Wing {rep:"FFEW"})

MATCH (sfew:Wing {rep:"SFEW"})

MATCH (a:Category { genre: "Fantasy"}) 
MATCH (b:Category { genre: "Adventure"}) 
MATCH (c:Category { genre: "Romance"}) 
MATCH (d:Category { genre: "Contemporary"}) 
MATCH (e:Category { genre: "Dystopian"}) 
MATCH (f:Category { genre: "Mystery"}) 
MATCH (g:Category { genre: "Horror"}) 
MATCH (h:Category { genre: "Thriller"}) 
MATCH (i:Category { genre: "Paranormal"}) 
MATCH (j:Category { genre: "Historical fiction"}) 
MATCH (k:Category { genre: "Science Fiction"}) 
MATCH (l:Category { genre: "Memoir"}) 
MATCH (m:Category { genre: "Cooking"}) 
MATCH (n:Category { genre: "Art"}) 
MATCH (o:Category { genre: "Self-help / Personal"}) 
MATCH (p:Category { genre: "Development"}) 
MATCH (q:Category { genre: "Motivational"}) 
MATCH (r:Category { genre: "Health"}) 
MATCH (s:Category { genre: "History"}) 
MATCH (t:Category { genre: "Travel"}) 
MATCH (u:Category { genre: "Guide / How-to"}) 
MATCH (v:Category { genre: " Families & Relationships"}) 
MATCH (w:Category { genre: "Humor"}) 
MATCH (x:Category { genre: "Children’s"})

MERGE (gew)<-[:PLACED_AT]-(a)
MERGE (gew)<-[:PLACED_AT]-(b)
MERGE (gew)<-[:PLACED_AT]-(c)

MERGE (gww)<-[:PLACED_AT]-(d)
MERGE (gww)<-[:PLACED_AT]-(e)
MERGE (gww)<-[:PLACED_AT]-(f)

MERGE (gsw)<-[:PLACED_AT]-(g)
MERGE (gsw)<-[:PLACED_AT]-(h)
MERGE (gsw)<-[:PLACED_AT]-(i)

MERGE (gnw)<-[:PLACED_AT]-(j)
MERGE (gnw)<-[:PLACED_AT]-(k)

MERGE (gfew)<-[:PLACED_AT]-(l)
MERGE (gfew)<-[:PLACED_AT]-(m)

MERGE (few)<-[:PLACED_AT]-(n)
MERGE (few)<-[:PLACED_AT]-(o)

MERGE (fww)<-[:PLACED_AT]-(p)
MERGE (fww)<-[:PLACED_AT]-(q)

MERGE (few)<-[:PLACED_AT]-(r)
MERGE (fww)<-[:PLACED_AT]-(s)

MERGE (sfew)<-[:PLACED_AT]-(t)
MERGE (sfew)<-[:PLACED_AT]-(u)

MERGE (ffew)<-[:PLACED_AT]-(v)
MERGE (ffew)<-[:PLACED_AT]-(w)
MERGE (ffew)<-[:PLACED_AT]-(x)


// #BOOKS

MATCH (a:Category { genre: "Fantasy"}) 
MATCH (b:Category { genre: "Adventure"}) 
MATCH (c:Category { genre: "Romance"}) 
MATCH (d:Category { genre: "Contemporary"}) 
MATCH (e:Category { genre: "Dystopian"}) 
MATCH (f:Category { genre: "Mystery"}) 
MATCH (g:Category { genre: "Horror"}) 
MATCH (h:Category { genre: "Thriller"}) 
MATCH (i:Category { genre: "Paranormal"}) 
MATCH (j:Category { genre: "Historical fiction"}) 
MATCH (k:Category { genre: "Science Fiction"}) 
MATCH (l:Category { genre: "Memoir"}) 
MATCH (m:Category { genre: "Cooking"}) 
MATCH (n:Category { genre: "Art"}) 
MATCH (o:Category { genre: "Self-help / Personal"}) 
MATCH (p:Category { genre: "Development"}) 
MATCH (q:Category { genre: "Motivational"}) 
MATCH (r:Category { genre: "Health"}) 
MATCH (s:Category { genre: "History"}) 
MATCH (t:Category { genre: "Travel"}) 
MATCH (u:Category { genre: "Guide / How-to"}) 
MATCH (v:Category { genre: " Families & Relationships"}) 
MATCH (w:Category { genre: "Humor"}) 
MATCH (x:Category { genre: "Children’s"})


MATCH (Ba:Book {Name: "Harry Potter and the Half-Blood Prince (Harry Potter, #6)"})
MATCH (Bb:Book {Name: "Harry Potter and the Order of the Phoenix (Harry Potter, #5)"})
MATCH (Bc:Book {Name: "Harry Potter and the Sorcerer's Stone (Harry Potter, #1)"})
MATCH (Bd:Book {Name: "Harry Potter and the Chamber of Secrets (Harry Potter, #2)"})
MATCH (Be:Book {Name: "Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)"})
MATCH (Bg:Book {Name: "Harry Potter and the Goblet of Fire (Harry Potter, #4)"})
MATCH (Bf:Book {Name: "Harry Potter Boxed Set, Books 1-5 (Harry Potter, #1-5)"})
MATCH (Bg:Book {Name: "The Ultimate Hitchhiker's Guide: Five Complete Novels and One Story (Hitchhiker's Guide to the Galaxy, #1-5)"})
MATCH (Bh:Book {Name: "The Ultimate Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy, #1-5)"})
MATCH (Bi:Book {Name: "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy, #1)"})
MATCH (Bj:Book {Name: "The Ultimate Hitchhiker's Guide (Hitchhiker's Guide to the Galaxy, #1-5)"})
MATCH (Bk:Book {Name: "A Short History of Nearly Everything"})
MATCH (Bl:Book {Name: "Bill Bryson's African Diary"})
MATCH (Bm:Book {Name: "Bryson's Dictionary of Troublesome Words: A Writer's Guide to Getting It Right"})
MATCH (Bn:Book {Name: "In a Sunburned Country"})
MATCH (Bo:Book {Name: "I'm a Stranger Here Myself: Notes on Returning to America After Twenty Years Away"})
MATCH (Bp:Book {Name: "The Lord of the Rings (The Lord of the Rings, #1-3)"})
MATCH (Bq:Book {Name: "The Fellowship of the Ring (The Lord of the Rings, #1)"})
MATCH (Br:Book {Name: "The Lord of the Rings: Weapons and Warfare"})
MATCH (Bs:Book {Name: "The Untouchables: Subordination, Poverty and the State in Modern India (Contemporary South Asia, #4)"})
MATCH (Bt:Book {Name: "Growing Up Untouchable in India: A Dalit Autobiography"})
MATCH (Bu:Book {Name: "The Complete Idiot's Guide to Motorcycles"})
MATCH (Bv:Book {Name: "Risotto: 30 Simply Delicious Vegetarian Recipes from an Italian Kitchen"})
MATCH (Bw:Book {Name: "The Americas in the Age of Revolutio: 1750-1850"})
MATCH (Bx:Book {Name: "Marketing: An Introduction"})

MERGE (Ba)-[:BELONGS_TO]->(a)
MERGE (Bb)-[:BELONGS_TO]->(a)
MERGE (Bc)-[:BELONGS_TO]->(a)
MERGE (Bd)-[:BELONGS_TO]->(a)
MERGE (Be)-[:BELONGS_TO]->(a)
MERGE (Bf)-[:BELONGS_TO]->(a)
MERGE (Bg)-[:BELONGS_TO]->(o)
MERGE (Bh)-[:BELONGS_TO]->(b)
MERGE (Bi)-[:BELONGS_TO]->(b)
MERGE (Bj)-[:BELONGS_TO]->(c)
MERGE (Bk)-[:BELONGS_TO]->(c)
MERGE (Bl)-[:BELONGS_TO]->(c)
MERGE (Bm)-[:BELONGS_TO]->(d)
MERGE (Bn)-[:BELONGS_TO]->(e)
MERGE (Bo)-[:BELONGS_TO]->(f)
MERGE (Bp)-[:BELONGS_TO]->(f)
MERGE (Bq)-[:BELONGS_TO]->(g)
MERGE (Br)-[:BELONGS_TO]->(h)
MERGE (Bs)-[:BELONGS_TO]->(i)
MERGE (Bt)-[:BELONGS_TO]->(j)
MERGE (Bu)-[:BELONGS_TO]->(k)
MERGE (Bv)-[:BELONGS_TO]->(l)
MERGE (Bw)-[:BELONGS_TO]->(m)
MERGE (Bx)-[:BELONGS_TO]->(n)


// # STUDENT ISSUE
MATCH (Ba:Book {Name: "Harry Potter and the Half-Blood Prince (Harry Potter, #6)"})
MATCH (Bb:Book {Name: "Harry Potter and the Order of the Phoenix (Harry Potter, #5)"})
MATCH (Bc:Book {Name: "Harry Potter and the Sorcerer's Stone (Harry Potter, #1)"})
MATCH (Bd:Book {Name: "Harry Potter and the Chamber of Secrets (Harry Potter, #2)"})
MATCH (Be:Book {Name: "Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)"})
MATCH (By:Book {Name: "Harry Potter and the Goblet of Fire (Harry Potter, #4)"})
MATCH (Bf:Book {Name: "Harry Potter Boxed Set, Books 1-5 (Harry Potter, #1-5)"})
MATCH (Bg:Book {Name: "The Ultimate Hitchhiker's Guide: Five Complete Novels and One Story (Hitchhiker's Guide to the Galaxy, #1-5)"})
MATCH (Bh:Book {Name: "The Ultimate Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy, #1-5)"})
MATCH (Bi:Book {Name: "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy, #1)"})
MATCH (Bj:Book {Name: "The Ultimate Hitchhiker's Guide (Hitchhiker's Guide to the Galaxy, #1-5)"})
MATCH (Bk:Book {Name: "A Short History of Nearly Everything"})
MATCH (Bl:Book {Name: "Bill Bryson's African Diary"})
MATCH (Bm:Book {Name: "Bryson's Dictionary of Troublesome Words: A Writer's Guide to Getting It Right"})
MATCH (Bn:Book {Name: "In a Sunburned Country"})
MATCH (Bo:Book {Name: "I'm a Stranger Here Myself: Notes on Returning to America After Twenty Years Away"})
MATCH (Bp:Book {Name: "The Lord of the Rings (The Lord of the Rings, #1-3)"})
MATCH (Bq:Book {Name: "The Fellowship of the Ring (The Lord of the Rings, #1)"})
MATCH (Br:Book {Name: "The Lord of the Rings: Weapons and Warfare"})
MATCH (Bs:Book {Name: "The Untouchables: Subordination, Poverty and the State in Modern India (Contemporary South Asia, #4)"})
MATCH (Bt:Book {Name: "Growing Up Untouchable in India: A Dalit Autobiography"})
MATCH (Bu:Book {Name: "The Complete Idiot's Guide to Motorcycles"})
MATCH (Bv:Book {Name: "Risotto: 30 Simply Delicious Vegetarian Recipes from an Italian Kitchen"})
MATCH (Bw:Book {Name: "The Americas in the Age of Revolutio: 1750-1850"})
MATCH (Bx:Book {Name: "Marketing: An Introduction"})


MATCH (a:Staff {Name: "Amethyst Macias"}) 
MATCH (b:Staff {Name: "Walker Vinson"})
MATCH (c:Staff {Name: "Allen Higgins"})
MATCH (d:Staff {Name: "Abbot Page"})
MATCH (e:Staff {Name: "Yardley Morris"})
MATCH (f:Staff {Name: "Cullen Campos"})
MATCH (g:Staff {Name: "Ina Terry"})

MATCH (sg:Student {Name: "Brandon Wiley"})
MATCH (sa:Student {Name: "Sylvester Jackson"})
MATCH (sb:Student {Name: "Lysandra Bell"})
MATCH (sc:Student {Name: "Ashely Pittman"})
MATCH (sd:Student {Name: "Vaughan Barnes"})
MATCH (se:Student {Name: "Serina Delgado"})
MATCH (sf:Student {Name: "Gisela Mcfarland"})

MERGE (a)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Ba)
MERGE (b)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bb)
MERGE (c)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bc)
MERGE (d)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bd)
MERGE (e)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Be)
MERGE (f)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bf)
MERGE (g)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bg)

MERGE (sa)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bh)
MERGE (sb)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bi)
MERGE (sc)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bj)
MERGE (sd)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bk)
MERGE (se)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bl)
MERGE (sf)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bm)
MERGE (sg)-[:HAS_ISSUED {issue_date: datetime(), deadline_date: datetime() + duration("P30D")}]->(Bn)

// DEPARTMENT AND SCHOOL

MATCH (n:Department) where n.Name= "Computer" OR n.Name= "Mechanical" OR n.Name= "Electrical" OR n.Name= "Civil"  
MATCH (s:School {ref:"SoE"})
MERGE (n)-[:DEPARTMENT_OF]->(s)

// MATCH (n:Department) where NOT IN (n.Name= "Computer" AND n.Name= "Mechanical" AND n.Name= "Electrical" AND n.Name= "Civil")


