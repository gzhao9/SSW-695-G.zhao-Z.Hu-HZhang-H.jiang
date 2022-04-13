import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import { useLocation } from "react-router-dom";
import Header from "../../Components/Header/Header";
import { Button, Input, InputNumber, Form } from "antd";

export default function ExerciseDetailPage() {
  const { state } = useLocation();
  const { exerciseInfo, isAdd, userID, date } = state;
  const { exercise_name, minute, calorie } = exerciseInfo;
  function onFinish(values) {
    console.log("Success:", values);
  }
  function onFinishFailed(errorInfo) {
    console.log("Failed:", errorInfo);
  }
  return (
    <div>
      <Header headerText="Exercise Setting" />
      <Form
        name="exerciseSetting"
        labelCol={{
          span: 3,
        }}
        wrapperCol={{
          span: 6,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
      >
        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Exercise Name"
          name="exerciseName"
          initialValue={exercise_name}
          rules={[
            {
              required: true,
              message: "Please input the exercise name!",
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Minute"
          name="minute"
          initialValue={minute}
          rules={[
            {
              required: true,
              message: "Please input the time you cost!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>
        <Form.Item
          style={{ marginLeft: "10%", marginRight: "10%" }}
          label="Calorie (kcal)"
          name="calorie"
          initialValue={calorie}
          rules={[
            {
              required: true,
              message: "Please input the calorie you consume!",
            },
          ]}
        >
          <InputNumber
            style={{ float: "left" }}
            min={0}
            max={10000}
            precision={2}
          />
        </Form.Item>
        <br />

        <Form.Item
          wrapperCol={{
            offset: 0,
            span: 16,
          }}
        >
          <Button
            type="primary"
            htmlType="submit"
            style={{
              width: "80%",
              height: "50px",
              borderRadius: "25px",
              bottom: "20px",
              marginTop: "10%",
            }}
          >
            {state.isAdd ? "Add Exercise" : "Change Exercise Info"}
          </Button>

          {!state.isAdd ? (
            <Form.Item
              wrapperCol={{
                offset: 0,
                span: 16,
              }}
            >
              <Button
                type="primary"
                style={{
                  width: "80%",
                  height: "50px",
                  borderRadius: "25px",
                  bottom: "20px",
                  marginTop: "5%",
                }}
              >
                Delete Exercise
              </Button>
            </Form.Item>
          ) : null}
        </Form.Item>
      </Form>
    </div>
  );
}
