import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Row, Col, Space, Modal } from "antd";
import { DeleteOutlined } from "@ant-design/icons";
import axios from "axios";

export default function ExerciseInfo(props) {
  const { exercise_name, minute, calorie, sportRecordId } = props.exerciseInfo;
  const [isModalVisible, setIsModalVisible] = useState(false);
  const navigate = useNavigate();
  const showModal = () => {
    setIsModalVisible(true);
  };
  const handleOk = () => {
    axios.post("/delete_Exercise", { sportRecordId: sportRecordId });

    setIsModalVisible(false);
    window.location.reload();
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
        <p>Are you sure you want to delete this exercise record?</p>
      </Modal>
      <Row justify="space-between">
        <Col span={12}>
          <span className="foodNameText">
            {exercise_name} <br />
            {minute} minutes
          </span>
        </Col>
        <Col span={6}>{calorie} kcal</Col>
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
