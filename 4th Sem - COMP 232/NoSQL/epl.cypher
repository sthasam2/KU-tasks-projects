// LOADING DATA INTO A RAW GRAPH
LOAD CSV
WITH HEADERS FROM 'file:///epl.csv' AS row
MERGE (n:RawData {
  Div:row.Div, 
  Date: row.Date, 
  HomeTeam: row.HomeTeam, 
  AwayTeam: row.AwayTeam, 
  FullTimeHomeGoal: row.FTHG, 
  FullTimeAwayGoal: row.FTAG, 
  FullTimeResult: row.FTR, 
  HalfTimeHomeGoal: row.HTHG, 
  HalfTimeAwayGoal: row.HTAG, 
  HalfTimeResult: row.HTR, 
  Referee: row.Referee, 
  HomeShot:row.HS, 
  AwayShot:row. AS, 
  HomeShotTarget:row.HST, 
  AwayShotTarget:row.AST, 
  HomeFoul: row.HF, 
  AwayFoul:row.AF, 
  HomeCorner:row.HC, 
  AwayCorner: row.AC, 
  HomeYellow:row.HY, 
  AwayYellow:row.AY, 
  HomeRed: row.HR, 
  AwayRed:row.AR
});

// UPDATE THE STRING DATE OF RAW DATA TO NEO4J READABLE DATE
MATCH (n:RawData)
WITH [item IN split(n.Date, "/") | toInteger(item)] AS dateComponents, n
SET n.Date = date({day: dateComponents[0], month: dateComponents[1], year: dateComponents[2]})
RETURN n;

// SETTING WEEKDAY AS DayOfWeek which ranges 1-7
WITH 1 being Monday
MATCH (n:RawData)
WITH n.Date AS d, n
SET n.DayOfWeek = n.Date.dayOfWeek
RETURN n
LIMIT 5;


//CREATING NODES

//Division of League
MATCH (n:RawData)
WITH DISTINCT n.Div AS Div
CREATE (d:Division {
  name: Div,
  season: "2018/2019"
});


//Teams
MATCH (n:RawData)
WITH DISTINCT n.HomeTeam AS HT
CREATE (d:Team {
  name: HT,
  matches_played: 0,
  won: 0,
  loss: 0,
  draw: 0,
  points: 0,
  home:0,
  away:0
});


//Matchday
//Matchday
MATCH (n:RawData)
CREATE (d:Matchday {
  title:n.HomeTeam+" vs. "+n.AwayTeam, 
  Date:n.Date, 
  HT:n.HomeTeam, 
  AT:n.AwayTeam, 
  REF:n.Referee
});

//away team
MATCH (m:Matchday)
MATCH (t:Team)
WHERE m.AT = t.name
MERGE (m)<-[:Away_Game]-(t);

//hometeam
MATCH (m:Matchday)
MATCH (t:Team)
WHERE m.HT = t.name
MERGE (m)<-[:Home_Game]-(t);


// division-has_match->matchday
MATCH (m:Division)
MATCH (n:Matchday)
MERGE (m)-[:has_Match]-(n);


//Results
MATCH (n:RawData)
MATCH (m:Matchday)
WHERE n.Date = m.Date AND n.HomeTeam = m.HT
MERGE (m)-[:has_Results]->(d:Results {
  FTHG:n.FullTimeHomeGoal,
  FTAG:n.FullTimeAwayGoal,
  FTR:n.FullTimeResult,
  HTHG:n.HalfTimeHomeGoal,
  HTAG:n.HalfTimeAwayGoal,
  HTR:n.HalfTimeResult
});


//Statistics
MATCH (n:RawData)
MATCH (m:Matchday)
WHERE n.Date = m.Date AND n.HomeTeam = m.HT
MERGE (m)-[:has_Statistics]->(d:Stats {
  HS:n.HomeShot, 
  AS :n.AwayShot, 
  HST:n.HomeShotTarget, 
  AST:n.AwayShotTarget,
  HF:n.HomeFoul, 
  AF:n.AwayFoul, 
  HC:n.HomeCorner, 
  AC:n.AwayCorner, 
  HY:n.HomeYellow, 
  AY:n.AwayYellow, 
  HR:n.HomeRed, 
  AR:n.AwayRed  
});

//Home stats
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[h:Home_Game]-(t:Team)
WHERE m1.Date=m.Date AND m1.HT = m.HT AND m1.AT = m.AT
SET h.HTG=r.HTHG, h.FTG=r.FTHG;
MATCH (m2:Matchday)-->(s:Stats)
MATCH (m1:Matchday)<-[h:Home_Game]-(t:Team)
WHERE m2.Date=m1.Date AND m2.HT = m1.HT AND m2.AT = m1.AT
SET h.S=s.HS, h.F=s.HF, h.ST=s.HST, h.C=s.HC, h.Y=s.HY, h.R=s.HR;

//Away stats
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[h:Away_Game]-(t:Team)
WHERE m1.Date=m.Date AND m1.AT = m.AT AND m1.HT = m.HT
SET h.HTG=r.HTAG, h.FTG=r.FTAG;
MATCH (m2:Matchday)-->(s:Stats)
MATCH (m1:Matchday)<-[h:Away_Game]-(t:Team)
WHERE m2.Date=m1.Date AND m2.AT = m1.AT AND m2.HT = m1.HT
SET h.S=s. AS , h.F=s.AF, h.ST=s.AST, h.C=s.AC, h.Y=s.AY, h.R=s.AR;


//QUERIES

//1.
MATCH (n:RawData)
WITH DISTINCT n.HomeTeam AS Team
RETURN Team ORDER BY Team ASC;


//2.
MATCH (n:Matchday)
WHERE n.Date.DayOfWeek = 1
RETURN COUNT(n) as Toatal_matches_on_Monday;


//3.
MATCH p=(m:Matchday)-[:has_Results]->(r:Results)
WHERE (m.HT="Man United" AND r.FTR="A") OR (m.AT="Man United" AND r.FTR="H")
RETURN m.Date as Date, m.HT as Home_Team, toInteger(r.FTHG) as Home_Score, toInteger(r.FTAG) as Away_Score, m.AT as Away_Team;


//4.
MATCH p=(m:Matchday)-[:has_Results]->(r:Results)
WHERE
(m.HT="Liverpool" AND r.HTR="A" AND r.FTR="H" )
OR
(m.AT="Liverpool" AND r.HTR="H" AND r.FTR="A")
RETURN m.Date AS Date, m.AT AS Away_Team , toInteger(r.HTAG) AS HT_Away_Goal, toInteger(r.FTAG) AS FT_Away_Goal, m.HT AS Home_Team, toInteger(r.HTHG) AS HT_Home_Goal, toInteger(r.FTHG) AS FT_Home_Goal


//5.

//SET win/loss home
//home win
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[:Away_Game|:Home_Game]-(t:Team)
WHERE (m.Date = m1.Date AND m.HT = m1.HT AND m.AT = m1.AT) AND r.FTR = "H" AND t.name = m.HT
SET t.won = (t.won+1), t.points = (t.points+3), t.matches_played = (t.matches_played+1), t.home=(t.home+1);
//away loss
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[:Away_Game|:Home_Game]-(t:Team)
WHERE (m.Date = m1.Date AND m.HT = m1.HT AND m.AT = m1.AT) AND r.FTR = "H" AND t.name = m.AT
SET t.loss = (t.loss+1), t.matches_played = (t.matches_played+1);

//SET win/loss away
//away win
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[:Away_Game|:Home_Game]-(t:Team)
WHERE (m.Date = m1.Date AND m.HT = m1.HT AND m.AT = m1.AT) AND r.FTR = "A" AND t.name = m.AT
SET t.won = (t.won+1), t.points = (t.points+3), t.matches_played = (t.matches_played+1), t.away=(t.away+1);
//home Loss
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[:Away_Game|:Home_Game]-(t:Team)
WHERE (m.Date = m1.Date AND m.HT = m1.HT AND m.AT = m1.AT) AND r.FTR = "A" AND t.name = m.HT
SET t.loss = (t.loss+1), t.matches_played = (t.matches_played+1);

//SET draw home
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[:Away_Game|:Home_Game]-(t:Team)
WHERE (m.Date = m1.Date AND m.HT = m1.HT AND m.AT = m1.AT) AND r.FTR = "D" AND t.name = m.HT
SET t.draw = (t.draw+1), t.points = (t.points+1), t.matches_played = (t.matches_played+1);
//SET away draw
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[:Away_Game|:Home_Game]-(t:Team)
WHERE (m.Date = m1.Date AND m.HT = m1.HT AND m.AT = m1.AT) AND r.FTR = "D" AND t.name = m.AT
SET t.draw = (t.draw+1), t.points = (t.points+1), t.matches_played = (t.matches_played+1);

//both team draw
MATCH (m:Matchday)-->(r:Results)
MATCH (m1:Matchday)<-[:Away_Game|:Home_Game]-(t:Team)
WHERE (m.Date = m1.Date AND m.HT = m1.HT AND m.AT = m1.AT) AND r.FTR = "D"
SET t.draw = (t.draw+1), t.points = (t.points+1), t.matches_played = (t.matches_played+1);

//Points Table
MATCH (t:Team)
RETURN t.name AS Team, t.matches_played AS Matches_Played, t.won AS Won, t.loss AS Lost, t.draw AS Draw, t.points AS Points
ORDER BY t.points DESC;
