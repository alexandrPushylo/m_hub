
$('#applications_container').masonry({
// указываем элемент-контейнер в котором расположены блоки для динамической верстки
    itemSelector: '.application_items',
    // columnWidth: 50,
    gutter: 20,
    fitWidth: true,
    horizontalOrder: false,
// указываем класс элемента являющегося блоком в нашей сетке
    singleMode: true,
// true - если у вас все блоки одинаковой ширины
    isResizable: true,
// перестраивает блоки при изменении размеров окна
    isAnimated: true,
// анимируем перестроение блоков
    animationOptions: {
        queue: false,
        duration: 500
    }
// опции анимации - очередь и продолжительность анимации
});

function closeDebt(e, debtId){
    $.ajax({
        type: 'POST',
        mode: 'same-origin',
        url: window.location,
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            debt_id: debtId
        }
    }).done((d) => {
        window.location.reload()
    })
}

function setDebtor(e){
    let debtorId = e.value;
    window.location.href = window.location.pathname + '?debtor_id='+debtorId;
}

function calculationOfDifferenceIndications(){
    const lastIndications = $('input[name="last_indications"]').val();
    const currentIndications = $('input[name="current_indications"]').val();
    const diffIndications = $('input[name="indications_diff"]');
    let diff = currentIndications - lastIndications;
    diffIndications.val(diff)
}
function calculationAmount() {
    const rate = $('input[name="rate"]').val();
    const diffIndications = $('input[name="indications_diff"]').val();
    const amount = $('input[name="amount"]');
    let proiz = rate * diffIndications;
    amount.val(proiz.toFixed(2))
}