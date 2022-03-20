import React from 'react'
import { Table } from 'antd'


export default function NutritionInfoBlock(props) {
    const {totalCarbo, totalFat, totalProtein} = props
    let totalWeight = totalCarbo+totalFat+totalProtein
    let carboRate = totalCarbo / totalWeight
    let fatRate = totalFat / totalWeight
    let proteinRate = totalProtein / totalWeight
    const column = [
        {
          title: 'Name',
          dataIndex: 'name',
          key: 'name',
        },
        {
          title: 'Rate (%)',
          dataIndex: 'rate',
          key: 'rate',
        },
        {
          title: 'Weight (g)',
          dataIndex: 'weight',
          key: 'weight',
        }]
    const dataSource = [
        {
          key: '1',
          name: 'Carbohydrates',
          rate: Math.round(carboRate * 10000) / 100,
          weight: Math.round(totalCarbo * 100) / 100
        },
        {
          key: '2',
          name: 'Proteins',
          rate: Math.round(proteinRate * 10000) / 100,
          weight: Math.round(totalProtein * 100) / 100
        },
        {
          key: '3',
          name: 'Fat',
          rate: Math.round(fatRate * 10000) / 100,
          weight: Math.round(totalFat * 100) / 100
        },
      ];
    return (
        <div>
            <Table columns={column} dataSource={dataSource} pagination={false}></Table>
        </div>
    )
}
