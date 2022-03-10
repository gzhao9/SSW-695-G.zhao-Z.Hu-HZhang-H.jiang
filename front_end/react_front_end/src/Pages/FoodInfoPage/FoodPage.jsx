import React from 'react'
import Header from '../../Components/Header/Header'
import FoodInfoList from '../../Components/FoodInfoList/FoodInfoList'
import CalorieInfoBlock from '../../Components/FoodInfoList/CalorieInfoBlock'
import NutritionInfoBlock from '../../Components/FoodInfoList/NutritionInfoBlock'
import JsonText from '../../Example_JSON/FOOD_INFO_EXAMPLE.json'
import './FoodPage.css'

export default function FoodPage() {
    let totalCalorie = 0
    let totalCarbo = 0
    let totalProtein = 0
    let totalFat = 0
    JsonText.map((item) => {
        totalCalorie += item.calorie_cost
        totalCarbo += item.carbohydrate
        totalProtein += item.protein
        totalFat += item.fat
    })
    totalCalorie = Math.round(totalCalorie * 100) / 100
    
    return (
        <div className='FoodInfoPg'>
            <Header headerText='Food Information'/>
            <FoodInfoList foodInfo={JsonText}/>
            <CalorieInfoBlock totalCalorie={totalCalorie}/>
            <NutritionInfoBlock totalCarbo={totalCarbo} totalFat={totalFat} totalProtein={totalProtein}/>
        </div>
    )
}
