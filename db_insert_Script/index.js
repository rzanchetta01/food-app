const db = require('mongoose')
const fs = require('fs')


db
.connect('mongodb+srv://admin:aiJ9uIFNBJeOfL0O@apirpg.zmnvg.mongodb.net/Foods_Proj?retryWrites=true&w=majority')
.then(
    console.log('banco connectado')
).catch(err => console.log(err))


const folder_path = '/home/rodrigozanchetta/PROJECTS/DIMAS_MOBILE_APP/food-app/web scrapper/links/foods'
const datas = fs.readdirSync(folder_path)

let foods = []

datas.forEach(food => {
    foods.push(folder_path + "/" + food)
})


const food_Schema = new db.Schema({}, { strict: false })
let food = db.model('foods', food_Schema)

foods.forEach(f => {
    const json = require(f)
    const food_data = new food(json)
    food_data.save()
})


