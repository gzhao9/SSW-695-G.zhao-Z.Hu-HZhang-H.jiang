import React from "react";
import { useNavigate } from "react-router-dom";
import { Row, Col, Space } from "antd";
import { RightOutlined } from "@ant-design/icons";
import "./FoodList.css";
import foodPic from "./example_pic.jpg";

export default function FoodInfo(props) {
  const { food_name, weight, calorie_cost } = props.foodInfo;
  const navigate = useNavigate();
  return (
    <div style={{ width: "100%" }}>
      <Row justify="space-between">
        <Col span={6}>
          <img src={foodPic} alt="Food Pic" className="foodPic" />
        </Col>
        <Col span={6}>
          <span className="foodNameText">
            {food_name} <br />
            {weight} gram
          </span>
        </Col>
        <Col span={6}>{calorie_cost} kcal</Col>
        <Col span={6}>
          <RightOutlined
            onClick={() => {
              navigate("/foodDetailPage", {
                state: { isAdd: false, foodInfo: props.foodInfo },
              });
            }}
          />
        </Col>
      </Row>
    </div>
  );
}
