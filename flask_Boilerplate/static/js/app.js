var HelloMessage = (function(_React$Component) {
  _inherits(HelloMessage, _React$Component);

  function HelloMessage() {
    _classCallCheck(this, HelloMessage);

    return _possibleConstructorReturn(
      this,
      (HelloMessage.__proto__ || Object.getPrototypeOf(HelloMessage)).apply(
        this,
        arguments
      )
    );
  }

  _createClass(HelloMessage, [
    {
      key: "render",
      value: function render() {
        return React.createElement("div", null, "Hello ", this.props.name);
      }
    }
  ]);

  return HelloMessage;
})(React.Component);

ReactDOM.render(
  React.createElement(HelloMessage, { name: "Taylor" }),
  mountNode
);
