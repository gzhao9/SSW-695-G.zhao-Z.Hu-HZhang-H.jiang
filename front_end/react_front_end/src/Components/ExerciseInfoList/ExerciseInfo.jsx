import React from "react";
import { useNavigate } from "react-router-dom";
import { Row, Col, Space } from "antd";
import { RightOutlined } from "@ant-design/icons";

export default function ExerciseInfo(props) {
  const { exercise_name, minute, calorie } = props.exerciseInfo;
  const navigate = useNavigate();
  return (
    <div style={{ width: "100%" }}>
      <Row justify="space-between">
        <Col span={12}>
          <span className="foodNameText">
            {exercise_name} <br />
            {minute} minutes
          </span>
        </Col>
        <Col span={6}>{calorie} kcal</Col>
        <Col span={6}>
          <RightOutlined
            onClick={() => {
              navigate("/exerciseDetailoPage", {
                state: {
                  isAdd: false,
                  exerciseInfo: props.exerciseInfo,
                  date: props.date,
                  userID: props.userID,
                },
              });
            }}
          />
        </Col>
      </Row>
    </div>
  );
}
