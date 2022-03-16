import React, { Component } from 'react'
import { Button, PageHeader, Form, Input, InputNumber } from 'antd';
import Header from '../../Components/Header/Header';
import './GetUserInfoPage.css'

export default class GetUserInfoPage extends Component {

  onFinish = (values) => {
    console.log('Success:', values);
  }

  onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  }
  render() {
    return (
      <div className='getUserInfoPg'>
         <Header headerText='Get User Info Page' />
          <Form
            name="basic"
            labelCol={{
              span: 3,
            }}
            wrapperCol={{
              span: 6,
            }}
            onFinish={this.onFinish}
            onFinishFailed={this.onFinishFailed}
            autoComplete="off"
          >
            <Form.Item
              style={{marginLeft: '10%', marginRight: '10%'}}
              
              label="Full Name"
              name="fullName"
              rules={[
                {
                  required: true,
                  message: 'Please input your name!',
                },
              ]}
            >
              <Input/>
            </Form.Item>

            <Form.Item
              style={{marginLeft: '10%', marginRight: '10%'}}
              
              label="Age"
              name="age"
              rules={[
                {
                  required: true,
                  message: 'Please input your age!',
                },
              ]}
            >
              <InputNumber
                style={{float: 'left'}}
                min={0}
                max={150}
                precision={0}
              />
            </Form.Item>

            <Form.Item
              style={{marginLeft: '10%', marginRight: '10%'}}
              
              label="Height (cm)"
              name="height"
              rules={[
                {
                  required: true,
                  message: 'Please input your height!',
                },
              ]}
            >
              <InputNumber
                style={{float: 'left'}}
                min={0}
                max={500}
                precision={2}
              />
            </Form.Item>

            <Form.Item
              style={{marginLeft: '10%', marginRight: '10%'}}
              
              label="Weight (kg)"
              name="weight"
              rules={[
                {
                  required: true,
                  message: 'Please input your weight!',
                },
              ]}
            >
              <InputNumber
                style={{float: 'left'}}
                min={0}
                max={1000}
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
              <Button type="primary" htmlType="submit" style={{width: '80%', height:'50px', borderRadius:'25px'}}>
                Submit
              </Button>
            </Form.Item>
          </Form>
      </div>
    )
  }
}
