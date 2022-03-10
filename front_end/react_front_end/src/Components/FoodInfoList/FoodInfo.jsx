import React from 'react'
import './FoodList.css'
import foodPic from './example_pic.jpg'


export default function FoodInfo(props) {
    const {food_name, weight, calorie_cost} = props.foodInfo
    return (
        <div className='foodInfoItem'>
            <span className='foodPic'><img src={foodPic} alt="Food Pic" className='foodPic' /></span>
            <span className='foodNameText'>
                {food_name}<br/>
                {weight} gram
            </span>
            <span className='foodCalorieText'>
                {calorie_cost} kcal
            </span>
        </div>
    )
}
