import React, { Component } from 'react'
import {PageHeader, Affix} from 'antd';
import {LeftCircleTwoTone} from '@ant-design/icons';
import './Header.css'

export default class Header extends Component {
  render() {
    const {headerText} = this.props
    const headerTextInfo = <span style={{color: '#DFDFDF'}}>{headerText}</span>
    return (<div>
        <Affix offsetTop={0}>
          <PageHeader
            className="site-page-header"
            onBack={() => window.history.back()}
            backIcon={<LeftCircleTwoTone twoToneColor={'#DFDFDF'} />}
            title={headerTextInfo}
            ghost={false}
            style={{border: '1px solid rgb(235, 237, 240)'}}
          />
        </Affix>
        
    </div>
    )
  }
}
