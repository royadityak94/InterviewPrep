` Structure of restaurants collection:
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
`
`Problem: display all the documents in the collection restaurants
Explanation: 
`
{
    db.restaurants.find();
}

`Problem: display the fields restaurant_id, name, borough and cuisine for all the documents in the collection
Explanation: 
`
{
    db.restaurants.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1});
}
`Problem: display the fields restaurant_id, name, borough and cuisine, and zipcode but exclude field _id for all the documents in the collection
Explanation: 
`
{
    db.restaurants.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1, "address.zipcode": 1, "_id": 0});
}
`Problem: Display the first 5 restaurants of borough Bronx
Explanation: 
`
{
    db.restaurants.find({'borough': 'Bronx'}).limit(5);
}
`Problem: Display the second 5 restaurants of borough Bronx after skipping first 5
Explanation: 
`
{
    db.restaurants.find({'borough': 'Bronx'}).skip(5).limit(5);
}
`Problem: find the restaurants who achieved a score more than 90 (GOOD)
Explanation: 
`
{
    db.restaurants.find({
        'grades': { $eleMatch: 
                    {"score": {$gt: 90}}
                }
    })
}
`Problem: find the restaurants that achieved a score, more than 80 but less than 100 (GOOD)
Explanation: 
`
{
    db.restaurants.find({'grades.score': {
        $or: [
            {'gt': 80},
            {'lt': 100}
        ]
        -- Can also be written as: $or: {$gt: 80, $lt: 100}
    }})
}
`Problem: find the restaurants which locate in latitude value less than -95.754168
Explanation: 
`
{
    db.restaurants.find({'address.coord.1': {$lt: -95.754168}}) -- 0 based indexing, (long, lat)
}
`Problem:  find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 
    and latitude less than -65.754168
Explanation: 
`
{
    db.restaurants.find({
        $and: [
            {"cuisine": {$ne: "American"}}, 
            {"grades": {$eleMatch: {"score": {$gt: 70}}}, 
            {"address.coord": {$lt: 70}}
        ]
    })
    -- Another way
    db.restaurants.find({
        "cuisine": {$ne: "American"}, 
        "grades.score": {$gt: 70},
        "address.coord": {$lt: -65.754168}
    });
}
`Problem: find the restaurants which do not prepare any cuisine of 'American' and achieved a grade point 'A' not belongs to the borough Brooklyn. 
The document must be displayed according to the cuisine in descending order
Explanation: 
`
{
    db.restaurants.find({
        $and: [
            {"cuisine": {$ne: "American"}}, 
            {"grades": {$eleMatch: {"grade": "A"}}}, 
            {"borough": {$ne: "Bronx"}}
        ]
    }).sort({"cuisine": -1})
}

`Problem: MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain
    - 'Wil' as first three letters for its name
    -  'ces' as last three letters for its name.
     'Reg' as three letters somewhere in its name
Explanation: 
`
{
    db.restaurants.find({
        $or: [
            {"name": /^Wil^/},
            {"name": /ces$/}, 
            {"name": /.*Reg.*/}
        ]}, 
        {"restaurant_id": 1, "borough": 1, "cuisine": 1, "_id": 0}
    )
}
`Problem: find the restaurant Id, name, borough and cuisine for those restaurants which are 
    - not belonging to the borough: Staten Island or Queens or Bronx or Brooklyn,  
    - achieved a score which is not more than 10
Explanation: 
`
{
    db.restaurants.find({
        "borough": {$nin: ["Staten Island", "Queens", "Bronx", "Brooklyn"]}, 
        "grades": {$eleMatch: {"score": {$lte: 10}}}
    })
}
`Problem: find the restaurant Id, name and grades for those restaurants where the 2nd element of grades array contains a 
grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z"
Explanation: 
`
{
    db.restaurants.find({
        {"grades": {
            $and: 
                {$eleMatch: {"grade": "A"}}, 
                {$eleMatch: {"score": 9}}, 
                {$eleMatch: {"$date": ISODATE("2014-08-11T00:00:00Z")}}
        }
        }
    })
}
`Problem: name of the restaurants in descending along with all the columns.
Explanation: 
`
{
    db.restaurants.find().sort({"name": -1}) -- {"name": 1} for ascending
}
`Problem: query to match either of the following: 
    - whether all the addresses contains the street or not
    - where the coord field value is Double
    - returns 0 as a remainder after dividing the score by 7
Explanation: 
`
{
    db.restaurants.find({
        $or: [
            "address.street": {$exists: true},
            "address.coord": {$type: 1}, 
            "grades.score": {$mod: [7, 0]}
        ]
    })
}
`Problem: query to find the restaurant name, borough, longitude and attitude and cuisine for those restaurants which
    - contains 'mon' as three letters somewhere in its name (case insensitive)
    - contain 'Mad' as first three letters of its name.
Explanation: 
`
{
    db.restaurants.find({
        $or: [
            {"name": {$regex: /.*mon.*/i}},
            {"mad": {$regex: /^Mad/}}
        ]
    })
}
`  --------------------------------------- Summary Statistics  ---------------------------------------`
-- Group by Count (Take below Aggregation pipeline as collection) -> (GOOD)
-- GROUPBY(name, country), COUNT(*) totalcount, COUNT(city) totalCity, SUM(students.number) AS totalStudents, 
-- Tell about other aggregate functions
--    SORT(totalcount desc)
{
    db.universities.aggregate([
        {$group: {
            "_id": {"name": "$name", "country": "$country"},  --Groupby(name, country) -- Single groupby: {"id": "$name"}
            {"totalcount": {$sum: 1}}, -- COUNT(*)
            {"totalCity": {$count: "$city"}}, -- COUNT(city)
            {"totalStudents": {$sum: "$students.number"}}
        }
        }, 
        {$project: {"universityName": "$name", "universityCountry": "$country"}} -- Put other columns as well
        {$sort: {"totalcount": -1}}, 
        {$out: "aggregatedUniversitiesSummary"} - Upsert the results on a collection named aggregatedUniversitiesSummary
    ])
}

-- $count, $max, $min, $avg, $sum $push (to array)


`  --------------------------------------- Aggregation Pipeline  ---------------------------------------
Typical Stages: $match -> $group -> $sort
Each stage can use max 100MB of RAM, to enable shuffle from disk: db.collection.aggregate(pipeline, {allowDiskUse: true})
Ability to explain the query: db.collections.aggregate([pipeline], {explain: true} )
 --------------------------------------- --------------------------------------- ------------------------
`
`Example Collection
1. universities
{
  country : 'Spain',
  city : 'Salamanca',
  name : 'USAL',
  location : {
    type : 'Point',
    coordinates : [ -5.6722512,17, 40.9607792 ]
  },
  students : [
    { year : 2014, number : 24774 }, { year : 2015, number : 23166 }]
}
{
  country : 'Spain',
  city : 'Salamanca',
  name : 'UPSA',
  location : {
    type : 'Point',
    coordinates : [ -5.6691191,17, 40.9631732 ]
  },
  students : [
    { year : 2014, number : 4788 },{ year : 2015, number : 4821 },]
}
2. courses
{university : 'USAL', name : 'Computer Science', level : 'Excellent'}
{university : 'USAL', name : 'Electronics', level : 'Intermediate'}

insert_example: 
db.courses.insert([{}, {}])
`

`Problem: Aggregation Pipeline (Example-1)
query:University = 'USAL', Get summary of year (groupby) and count of students, Limit (top 10)
Explanation: filter on name, flatten students, then keep year and number, sort by descending and limit
`
{
    db.universities.aggrgate([
        {'$match': {"name": "USAL"}}, 
        {$unwind: "$students"}, -- Similar to exlode, each array is now part of an independent json
        {$project: {"_id": 0, "students.year": 1, "students.number": 1}}, 
        {$sort: {"students.number": -1}}, 
        {$limit: 10}
    ])

    -- Shortcut to above (i.e, grouping, counting and sorting in descending order)
    db.universities.aggregate([
        {$sortByCount: "$level"}
    ])

    -- Count of total students in the university: SUM(students.number) FROM students
    db.universities.aggregate([
        {$unwind: "$students"}, 
        {$count: 'total_students'}
    ]).pretty()
}

`Problem: Aggregation Pipeline (Example-2) - $lookup (merging two or more collections)
query:University =  For 'usal', bring in courses under universities collection in results 
`
{
    db.universities.aggregate([
        {$match: {"name": "USAL"}}, -- Filter only for university name = 'USAL'
        {$project: {"_id": 0, "name": 1}}, -- Get only name field
        {$lookup: { -- append courses based on universities.name = courses.university
            from: "courses", 
            localField: "name", -- field in universities
            foreignField: "university", --field in courses
            as: "courses"
        }}
    ])
}
`Problem: Total # of students belonging to each university, sorted by totalalumni(desc)
`
{
    db.universities.aggregate([
        {$unwind: "$students"}, 
        {$group: {"_id": "$name", "totalalumni": {$sum: "$students.number"}  }}, 
        {$sort: {"totalalumni": -1}}
    ]).pretty
}