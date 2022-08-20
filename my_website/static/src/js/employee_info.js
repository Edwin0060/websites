odoo.define('academy.add_value', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var core = require('web.core');
var _t = core._t;

var timeout;

//creating a new widget and adding our method to perform action. and registering to publicwidget
publicWidget.registry.addValue = publicWidget.Widget.extend({

//    Selction particular template class js taken to load only in particular section
    selector: '.oe_addvalue',



//    based on button class intializing  function
    events: {
        'click .addValueBtn': '_onAddValue',
    },


//   function called when we click sumbit button
     _onAddValue: function (ev) {

        var num1 = $("input[name='name']").val();
        var email = $("input[name='email_input']").val();
        var job_po = $("input[name='job_position']").val();
        console.log('eeeeeeeeeeeeeeeeeeeeeeeee',num1 ,email ,  job_po)

//         this rpc method calling python function and sending value as json format
        this._rpc({
            route: "/add/value/sum",
            params: {
                num1: num1,
            },
        })
//.then(function (data) {
////            data  received from python
//            $("input[name='sum']").val(data['sum'])
//        });

     },


});


return {
    AcademyAddValue: publicWidget.registry.addValue,
};

});
