import React, { useEffect, useState } from "react";
import {
  Avatar,
  Row,
  Col,
  Card,
  List,
  Skeleton,
  Button,
  DatePicker,
} from "antd";
import { UserOutlined } from "@ant-design/icons";
import { useLocation, Link } from "react-router-dom";
import axios from "axios";
import moment from "moment";
import Header from "../../Components/Header/Header";
import "../../UniversalStyle/UniversalStyle.css";

export default function UserInfoPage() {
  const { state } = useLocation();
  const { userId } = state;
  const [chosenDate, setChosenDate] = useState(moment().format("YYYY-MM-DD"));
  const [userData, setUserData] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    axios.post("/getUserInfo/" + userId, { date: chosenDate }).then((value) => {
      // setUserData(value.data);
      // setIsLoading(false);
      console.log(value.data);
    });
  }, [chosenDate]);
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
  function onDateChange(date, dateString) {
    setChosenDate(dateString);
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
          <Col span={8} className="shownText" style={{ textAlign: "left" }}>
            Hello, <br /> {userName}
          </Col>
          <Col span={8} style={{ textAlign: "left" }}>
            <Link style={{ color: "royalblue" }} to="/getUserInfoPage">
              View My Info
            </Link>
          </Col>
        </Row>
        <DatePicker
          placeholder="Please Input the Date"
          size="large"
          defaultValue={moment()}
          style={{ width: "80%", marginTop: "30px", marginBottom: "30px" }}
          onChange={onDateChange}
        ></DatePicker>
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
            <Link
              style={{ color: "royalblue" }}
              to="/foodPage"
              state={{ date: chosenDate }}
            >
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
