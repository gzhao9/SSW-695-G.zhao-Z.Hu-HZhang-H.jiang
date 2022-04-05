import React, { useEffect, useState } from "react";
import { Avatar, Row, Col, Card, List, Skeleton } from "antd";
import { UserOutlined } from "@ant-design/icons";
import { useLocation, Link } from "react-router-dom";
import axios from "axios";
import Header from "../../Components/Header/Header";
import "../../UniversalStyle/UniversalStyle.css";

export default function UserInfoPage() {
  // const { state } = useLocation();
  // const { userName } = state;
  const [userData, setUserData] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    axios.get("/readUserDate").then((value) => {
      setUserData(value.data);
      setIsLoading(false);
    });
  }, []);
  const { userName, avatar, mealInfo, remainedCalorie } = userData;
  let shownMealInfo = [];
  if (mealInfo) {
    if (mealInfo.length <= 3) {
      for (let i = 0; i < mealInfo.length; i++) {
        shownMealInfo.push(mealInfo[i].food_name);
      }
    } else {
      for (let i = 0; i < 3; i++) {
        shownMealInfo.push(mealInfo[i].food_name);
      }
      shownMealInfo.push("...");
    }
  }

  return (
    <div style={{ overflowY: "scroll" }}>
      <Header headerText="User Info" />
      <Skeleton
        avatar
        loading={isLoading}
        style={{
          marginLeft: "5%",
          marginRight: "5%",
          marginTop: "10%",
          width: "90%",
        }}
        active
      >
        <Row align="middle">
          <Col span={8}>
            <Avatar
              icon={<UserOutlined />}
              src={avatar}
              size={64}
              style={{ marginTop: "20px", marginBottom: "20px" }}
            />
          </Col>
          <Col span={16} className="shownText" style={{ textAlign: "left" }}>
            Hello, <br /> {userName}
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
          {remainedCalorie} kcal
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
            dataSource={shownMealInfo}
            renderItem={(item) => {
              return <List.Item>{item}</List.Item>;
            }}
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
      </Skeleton>
    </div>
  );
}
