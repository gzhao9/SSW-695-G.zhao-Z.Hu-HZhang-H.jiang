import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Row, Col, Space, Modal } from "antd";
import { DeleteOutlined } from "@ant-design/icons";
import "./FoodList.css";
import axios from "axios";
import foodPic from "./example_pic.jpg";

export default function FoodInfo(props) {
  const { food_name, weight, calorie_cost, mealRecordID } = props.foodInfo;
  const [isModalVisible, setIsModalVisible] = useState(false);
  const navigate = useNavigate();
  const showModal = () => {
    setIsModalVisible(true);
  };

  const handleOk = () => {
    axios.post("/delete_food", { mealId: mealRecordID });
    window.location.reload();
    setIsModalVisible(false);
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };
  return (
    <div style={{ width: "100%" }}>
      <Modal
        title="Warning"
        visible={isModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <p>Are you sure you want to delete this food?</p>
      </Modal>
      <Row justify="space-between">
        {/* <Col span={6}>
          <img src={foodPic} alt="Food Pic" className="foodPic" />
        </Col> */}
        <Col span={12}>
          <span className="foodNameText">
            {food_name} <br />
            {weight} gram
          </span>
        </Col>
        <Col span={6}>{calorie_cost} kcal</Col>
        <Col span={6}>
          <DeleteOutlined
            onClick={() => {
              showModal();
            }}
          />
        </Col>
      </Row>
    </div>
  );
}
