import React from 'react'

export default function CalorieInfoBlock(props) {
    const {totalCalorie} = props
    return (
        <div className='container'>
            <p className='foodNameText'>Total Calorie:</p>
            <p className='foodCalorieText'>{totalCalorie} kcal</p>
        </div>
    )
}
