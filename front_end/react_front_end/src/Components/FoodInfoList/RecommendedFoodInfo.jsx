import React from "react";
import { useNavigate } from "react-router-dom";
import { Row, Col } from "antd";
import { PlusCircleOutlined } from "@ant-design/icons";
import "./FoodList.css";

export default function RecommendedFoodInfo(props) {
  const { foodInfo, userID, date } = props;
  const { foodName } = foodInfo;
  const navigate = useNavigate();
  return (
    <div style={{ width: "100%" }}>
      <Row justify="space-between">
        <Col span={12} className="foodNameText">
          {foodName}
        </Col>
        <Col span={6}>
          <PlusCircleOutlined
            onClick={() => {
              navigate("/foodDetailPage", {
                state: { date: date, userID: userID, foodInfo: foodInfo },
              });
            }}
          />
        </Col>
      </Row>
    </div>
  );
}
