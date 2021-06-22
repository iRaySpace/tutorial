frappe.ui.form.on("Sales Invoice", {
  custom_discount_percentage: function (frm) {
    frm.doc.items.forEach((item) => {
      frappe.model.set_value(
        item.doctype,
        item.name,
        'discount_percentage',
        frm.doc.custom_discount_percentage,
      );
    });
  },
});
