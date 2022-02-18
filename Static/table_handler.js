
$(document).ready(function () {


    
    $('#customer_lising_table').DataTable({
      displayLength: 100,
      lengthMenu: [5, 10, 25, 50, 75, 100],

      'columnDefs': [
      {
        className: "control",
        orderable: !1,
        responsivePriority: 2,
        targets: 0
      }, {
        targets: 1,
        orderable: !1,
        responsivePriority: 3,
        render: function (e, t, a, s) {
          return '<div class="form-check"> <input class="form-check-input dt-checkboxes" type="checkbox" value="" id="checkbox' + e + '" /><label class="form-check-label" for="checkbox' + e + '"></label></div>'
        },
        checkboxes: {
          selectAllRender: '<div class="form-check"> <input class="form-check-input" type="checkbox" value="" id="checkboxSelectAll" /><label class="form-check-label" for="checkboxSelectAll"></label></div>'
        }
      },
      
      
      ],

      'select': {
        'style': 'multi'
      },
      'order': [
        [1, 'asc']
      ],




      buttons: [{
        text: feather.icons['plus'].toSvg({
          class: 'me-50 font-small-4'
        }) + 'Add New Record',
        className: 'create-new btn btn-primary',
        attr: {
          'data-bs-toggle': 'modal',
          'data-bs-target': '#modals-slide-in',
          'href': '/'
        },
        href: '/',
        init: function (api, node, config) {
          $(node).removeClass('btn-secondary');
        }
      }],
      responsive: {
        details: {
          display: $.fn.dataTable.Responsive.display.modal({
            header: function (row) {
              var data = row.data();
              return 'Details of ' + data['full_name'];
            }
          }),
          type: 'column',
          renderer: function (api, rowIdx, columns) {
            var data = $.map(columns, function (col, i) {
              return col.title !==
                '' // ? Do not show row in modal popup if title is blank (for check box)
                ?
                '<tr data-dt-row="' +
                col.rowIdx +
                '" data-dt-column="' +
                col.columnIndex +
                '">' +
                '<td>' +
                col.title +
                ':' +
                '</td> ' +
                '<td>' +
                col.data +
                '</td>' +
                '</tr>' :
                '';
            }).join('');

            return data ? $('<table class="table"/>').append('<tbody>' + data + '</tbody>') : false;
          }
        }
      },
      language: {
        paginate: {
          // remove previous & next text from pagination
          previous: '&nbsp;',
          next: '&nbsp;'
        }
      },
    });

    $('#frm-example').on('submit', function (e) {
      var form = this;

      var rows_selected = table.column(0).checkboxes.selected();

      // Iterate over all selected checkboxes
      $.each(rows_selected, function (index, rowId) {
        // Create a hidden element
        $(form).append(
          $('<input>')
          .attr('type', 'hidden')
          .attr('name', 'id[]')
          .val(rowId)
        );
      });
    });













 
        $('#enrolled_program_listing_table').DataTable({
          displayLength: 1,
          lengthMenu: [1,5, 10, 25, 50, 75, 100],
    
          'columnDefs': [
          {
            className: "control",
            orderable: !1,
            responsivePriority: 2,
            targets: 0
          }, {
            targets: 1,
            orderable: !1,
            responsivePriority: 3,
            render: function (e, t, a, s) {
              return '<div class="form-check"> <input class="form-check-input dt-checkboxes" type="checkbox" value="" id="checkbox' + e + '" /><label class="form-check-label" for="checkbox' + e + '"></label></div>'
            },
            checkboxes: {
              selectAllRender: '<div class="form-check"> <input class="form-check-input" type="checkbox" value="" id="checkboxSelectAll" /><label class="form-check-label" for="checkboxSelectAll"></label></div>'
            }
          },
          
          
          ],
    
          'select': {
            'style': 'multi'
          },
          'order': [
            [1, 'asc']
          ],
    
    
    
    
          buttons: [{
            text: feather.icons['plus'].toSvg({
              class: 'me-50 font-small-4'
            }) + 'Add New Record',
            className: 'create-new btn btn-primary',
            attr: {
              'data-bs-toggle': 'modal',
              'data-bs-target': '#modals-slide-in',
              'href': '/'
            },
            href: '/',
            init: function (api, node, config) {
              $(node).removeClass('btn-secondary');
            }
          }],
          responsive: {
            details: {
              display: $.fn.dataTable.Responsive.display.modal({
                header: function (row) {
                  var data = row.data();
                  return 'Details of ' + data['full_name'];
                }
              }),
              type: 'column',
              renderer: function (api, rowIdx, columns) {
                var data = $.map(columns, function (col, i) {
                  return col.title !==
                    '' // ? Do not show row in modal popup if title is blank (for check box)
                    ?
                    '<tr data-dt-row="' +
                    col.rowIdx +
                    '" data-dt-column="' +
                    col.columnIndex +
                    '">' +
                    '<td>' +
                    col.title +
                    ':' +
                    '</td> ' +
                    '<td>' +
                    col.data +
                    '</td>' +
                    '</tr>' :
                    '';
                }).join('');
    
                return data ? $('<table class="table"/>').append('<tbody>' + data + '</tbody>') : false;
              }
            }
          },
          language: {
            paginate: {
              // remove previous & next text from pagination
              previous: '&nbsp;',
              next: '&nbsp;'
            }
          },
        });
    
        $('#frm-example').on('submit', function (e) {
          var form = this;
    
          var rows_selected = table.column(0).checkboxes.selected();
    
          // Iterate over all selected checkboxes
          $.each(rows_selected, function (index, rowId) {
            // Create a hidden element
            $(form).append(
              $('<input>')
              .attr('type', 'hidden')
              .attr('name', 'id[]')
              .val(rowId)
            );
          });
        });
     
    


















  });



