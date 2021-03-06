import React from 'react';

import StockItem from './StockItem';

const StockList = (props) => {
  const { stocks } = props;

  const totalValue = (stock) => stock.amount * stock.info.quote.latestPrice;

  const stockItems = stocks
    .sort((stockA, stockB) => totalValue(stockB) - totalValue(stockA))
    .map((stock) => <StockItem key={stock.ticker} stock={stock} />);

  const totalAssetsValue = stocks.reduce((total, stock) => total + totalValue(stock), 0);

  return <>
    <div className="ui container segment">
      <h2 className="ui dividing header">
        Stock Holdings
        <div className="sub header">
          {`Total Assets: $${totalAssetsValue.toFixed(2)}`}
        </div>
      </h2>
      <table className="ui celled table">
        <thead>
          <tr>
            <th>Company</th>
            <th>Price</th>
            <th>Amount</th>
            <th>Total Value</th>
          </tr>
        </thead>
        <tbody>
          { stockItems }
        </tbody>
      </table>
    </div>
  </>;
};

export default StockList;