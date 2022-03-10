import React from 'react'
import FoodInfo from './FoodInfo'
import './FoodList.css'


export default function FoodInfoList(props) {
    return (
        <div className='foodInfoListItem'>
            {props.foodInfo.map((item, index) => {
                return <FoodInfo key={index} foodInfo={item}/>
            })}
        </div>
    )
}
