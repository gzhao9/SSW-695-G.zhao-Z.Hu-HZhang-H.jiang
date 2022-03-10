import React from 'react'
import '../../css/bootstrap.css'

export default function CalorieInfoBlock(props) {
    const {totalCalorie} = props
    return (
        <div className='container'>
            <p className='foodNameText'>Total Calorie:</p>
            <p className='foodCalorieText'>{totalCalorie} kcal</p>
        </div>
    )
}
