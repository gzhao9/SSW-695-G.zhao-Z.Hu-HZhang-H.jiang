import React from 'react'
import echarts from 'echarts/lib/echarts'


export default function NutritionInfoBlock(props) {
    const {totalCarbo, totalFat, totalProtein} = props
    let totalWeight = totalCarbo+totalFat+totalProtein
    let carboRate = totalCarbo / totalWeight
    let fatRate = totalFat / totalWeight
    let proteinRate = totalProtein / totalWeight
    return (
        <div className='container'>
            <span className='foodNameText'>
                Carbohydrates: <br/>
                Proteins: <br/>
                Fat: 
            </span>
            <span className='foodCalorieText'>
                {Math.round(carboRate * 10000) / 100}%,   {Math.round(totalCarbo * 100) / 100}g <br/>
                {Math.round(proteinRate * 10000) / 100}%,   {Math.round(totalProtein * 100) / 100}g <br/>
                {Math.round(fatRate * 10000) / 100}%,   {Math.round(totalFat * 100) / 100}g
            </span>
        </div>
    )
}
