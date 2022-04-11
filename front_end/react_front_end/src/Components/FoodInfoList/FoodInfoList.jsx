import React from "react";
import FoodInfo from "./FoodInfo";
import { List } from "antd";
import "./FoodList.css";

export default function FoodInfoList(props) {
  return (
    <div className="foodInfoListItem">
      <List
        bordered
        dataSource={props.foodInfo}
        renderItem={(item) => (
          <List.Item>
            <FoodInfo foodInfo={item} date={props.date} />
          </List.Item>
        )}
      />
    </div>
  );
}
