import React from "react";
import { Avatar, Row, Col, Card, List } from "antd";
import { UserOutlined } from "@ant-design/icons";
import { useLocation, Link } from "react-router-dom";
import axios from "axios";
import Header from "../../Components/Header/Header";
import "../../UniversalStyle/UniversalStyle.css";

export default function UserInfoPage() {
  // const { state } = useLocation();
  // const { userName } = state;

  return (
    <div>
      <Header headerText="User Info" />
      <Row align="middle">
        <Col span={8}>
          <Avatar
            icon={<UserOutlined />}
            size={64}
            style={{ marginTop: "20px", marginBottom: "20px" }}
          />
        </Col>
        <Col span={16} className="shownText" style={{ textAlign: "left" }}>
          Hello, <br /> userName
        </Col>
      </Row>
      <Card
        title="Remaining Calorie"
        type="inner"
        style={{
          width: "90%",
          marginLeft: "5%",
          marginRight: "5%",
          marginTop: "30px",
          marginBottom: "30px",
          textAlign: "center",
          fontSize: "50px",
          fontWeight: "bolder",
          color: "#2F4F4F",
        }}
        headStyle={{ textAlign: "left" }}
      >
        1000 kcal
      </Card>
      <Card
        title="My Meal"
        type="inner"
        style={{
          width: "90%",
          marginLeft: "5%",
          marginRight: "5%",
          marginTop: "30px",
          marginBottom: "30px",
          textAlign: "left",
        }}
        headStyle={{ textAlign: "left" }}
        extra={
          <Link style={{ color: "royalblue" }} to="/foodPage">
            View All
          </Link>
        }
      >
        <List
          size="small"
          dataSource={["111", "222", "333"]}
          renderItem={(item) => <List.Item>{item}</List.Item>}
        />
      </Card>
      <Card
        title="My Exercise"
        type="inner"
        style={{
          width: "90%",
          marginLeft: "5%",
          marginRight: "5%",
          marginTop: "30px",
          marginBottom: "30px",
          textAlign: "left",
        }}
        headStyle={{ textAlign: "left" }}
        extra={
          <Link style={{ color: "royalblue" }} to="/foodPage">
            View All
          </Link>
        }
      >
        <List
          size="small"
          dataSource={["111", "222", "333"]}
          renderItem={(item) => <List.Item>{item}</List.Item>}
        />
      </Card>
    </div>
  );
}
