## stock app

## About:
  An app that simulates the buying and selling of real time stocks

## Problem Statement:
   Need to be able to figure out how to pull real time stock data into an app, where the user can "buy and sell stocks". This will be kind of game where the user starts with x amount of money and is able to create a portfolio where he or she can add to the total money, or if bad stock choices are made, it will take away from the total money

## Assumptions:
   The assumptions will be the user will have some of knowledge on the stock they are trying to buy or sell. Can use a basic app interface

## Acceptance Criteria:
   To start off, the code needs to be able to pull real time stock data. So far in my research I have found using the panda datareader with Yahoo Finance the best way to do this. Then the code must ask to buy or sell. If buy is selected the app must deduct the value of the stocks and shares and subtract it from the total money and add stock to a portfolio. If sell is enabled then the app will need to sell the stock or stocks and add earnings back into the total amount correctly

## Features:
  Feature overview : A simple simulator where the user buy an sell stocks, adds to portfolio and the amount earned or loss is reflected in total money amount of user
   
   Feature 1(Buy): This is where the user will be able buy stocks using the tickr and the amount of shares and price will be subtracted from the users total money
  
   Feature 2(Sell): This is where the user can sell stocks from the purchased stocks and the earning or loss will be reflected to the users total money
  
  Feature 3(Portfolio): This is where the list stocks that the user owns will be reflected
