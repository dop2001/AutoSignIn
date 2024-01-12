## Introduction

​	This repository is a small tool for automatic sign-in, capable of performing the sign-in operation automatically at scheduled times each day. It mainly utilizes the Selenium library in Python for implementation, and the tool is triggered at scheduled intervals by deploying it in GitHub Actions.

## Scop of Use

​	It can only be used for the automatic sign-in service of [Gpushare Cloud](https://gpushare.com/)  website, and your account needs to be a V2 member.

## Deployment

- Clone this repository into your own account.

- Set repository variables.

  ```bash
  USERNAEM="Your username"
  PASSWORD="Your password"
  ```

- Execute the ***deployment.yml*** file in Actions to complete automatic deployment

