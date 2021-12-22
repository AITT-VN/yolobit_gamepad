/*

block 1: đọc joystick và gửi lệnh điều khiển 

block 2: đọc joystick [x | y | góc quay | khoảng cách kéo]

block 3: đọc trạng thái nút nhấn [C (dưới) | D (phải) | E (trên) | F (trái)]

*/
// Any imports need to be reserved words
Blockly.Python.addReservedWords('gamepad');

Blockly.Blocks['gamepad_read_drive'] = {
  init: function() {
    this.jsonInit(
      {"colour": "#1b80c4",
      "nextStatement": null, 
      "tooltip": "Đọc trạng thái Joystick và gửi lệnh điều khiển đến robot nếu đang kết nối", 
      "message0": "đọc joystick và gửi lệnh điều khiển di chuyển", 
      "previousStatement": null, 
      "args0": [],
      "helpUrl": ""});
  },
  getDeveloperVars: function() {
    return ['gamepad'];
  }
};

Blockly.Python['gamepad_read_drive'] = function(block) {
  Blockly.Python.definitions_['import_gamepad'] = 'from gamepad import *';
  // TODO: Assemble Python into code variable.
  var code = 'gamepad.read_drive()\n';
  return code;
};

Blockly.Blocks["gamepad_read_joystick"] = {
  init: function () {
    this.jsonInit({
      colour: "#1b80c4",
      tooltip: "",
      message0: "đọc joystick %1",
      args0: [
        {
          "type": "field_dropdown",
          "name": "input",
          "options": [
            [
              "X",
              "0"
            ],
            [
              "Y",
              "1"
            ],
            [
              "góc quay",
              "2"
            ],
            [
              "khoảng cách kéo",
              "3"
            ]
          ]
        }
      ],
      output: "Number",
      helpUrl: "",
    });
  },
  getDeveloperVars: function() {
    return ['gamepad'];
  }
};

Blockly.Python["gamepad_read_joystick"] = function (block) {
  var input = block.getFieldValue("input");
  // TODO: Assemble Python into code variable.
  Blockly.Python.definitions_['import_gamepad'] = 'from gamepad import *';
  var code = 'gamepad.read_joystick()[' + input + ']';
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Blocks["gamepad_read_buttons"] = {
  init: function () {
    this.jsonInit({
      colour: "#1b80c4",
      tooltip: "Kiểm tra nút trên GamePad có được nhấn hay không",
      message0: "nút %1 được nhấn",
      args0: [
        {
          "type": "field_dropdown",
          "name": "input",
          "options": [
            [
              "Joystick",
              "0"
            ],
            [
              "C",
              "1"
            ],
            [
              "D",
              "2"
            ],
            [
              "E",
              "3"
            ],
            [
              "F",
              "4"
            ]
          ]
        }
      ],
      output: null,
      helpUrl: "",
    });
  },
  getDeveloperVars: function() {
    return ['gamepad'];
  }
};

Blockly.Python["gamepad_read_buttons"] = function (block) {
  var input = block.getFieldValue("input");
  // TODO: Assemble Python into code variable.
  Blockly.Python.definitions_['import_gamepad'] = 'from gamepad import *';
  var code = 'gamepad.read_buttons()[' + input + ']';
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Blocks["gamepad_direction"] = {
  init: function () {
    this.jsonInit({
      type: 'gamepad_direction',
      tooltip: "Kiểm tra các hướng của joystick trên GamePad",
      colour: "#1b80c4",
      message0: "joystick ở hướng %1",
      args0: [
        {
          type: "field_dropdown",
          name: "dir",
          options: [
            [
              {
                "src": "https://ohstem-public.s3.ap-southeast-1.amazonaws.com/extensions/AITT-VN/yolobit_gamepad/images/arrow-right.svg",
                "width": 15,
                "height": 15,
                "alt": "phải"
              },
              "1"
            ],
            [
              {
                "src": "https://ohstem-public.s3.ap-southeast-1.amazonaws.com/extensions/AITT-VN/yolobit_gamepad/images/arrow-up-right.svg",
                "width": 15,
                "height": 15,
                "alt": "lên phải"
              },
              "2"
            ],
            [
              {
                "src": "https://ohstem-public.s3.ap-southeast-1.amazonaws.com/extensions/AITT-VN/yolobit_gamepad/images/arrow-up.svg",
                "width": 15,
                "height": 15,
                "alt": "lên"
              },
              "3"
            ],
            [
              {
                "src": "https://ohstem-public.s3.ap-southeast-1.amazonaws.com/extensions/AITT-VN/yolobit_gamepad/images/arrow-up-left.svg",
                "width": 15,
                "height": 15,
                "alt": "lên trái"
              },
              "4"
            ],
            [
              {
                "src": "https://ohstem-public.s3.ap-southeast-1.amazonaws.com/extensions/AITT-VN/yolobit_gamepad/images/arrow-left.svg",
                "width": 15,
                "height": 15,
                "alt": "trái"
              },
              "5"
            ],
            [
              {
                "src": "https://ohstem-public.s3.ap-southeast-1.amazonaws.com/extensions/AITT-VN/yolobit_gamepad/images/arrow-down-left.svg",
                "width": 15,
                "height": 15,
                "alt": "xuống trái"
              },
              "6"
            ],
            [
              {
                "src": "https://ohstem-public.s3.ap-southeast-1.amazonaws.com/extensions/AITT-VN/yolobit_gamepad/images/arrow-down.svg",
                "width": 15,
                "height": 15,
                "alt": "xuống"
              },
              "7"
            ],
            [
              {
                "src": "https://ohstem-public.s3.ap-southeast-1.amazonaws.com/extensions/AITT-VN/yolobit_gamepad/images/arrow-down-right.svg",
                "width": 15,
                "height": 15,
                "alt": "xuống phải"
              },
              "8"
            ],
          ],
        }
      ],
      output: null,
      helpUrl: ""
    });
  },
  getDeveloperVars: function() {
    return ['gamepad'];
  }
};

Blockly.Python['gamepad_direction'] = function(block) {
  var dir = block.getFieldValue("dir");
  Blockly.Python.definitions_['import_gamepad'] = 'from gamepad import *';
  var code = 'gamepad.check_dir(' + dir + ')';
  return [code, Blockly.Python.ORDER_NONE];
};

