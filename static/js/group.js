// $(document).ready(function() {
//     // page reload and add page
//     $('.column-teacher2').css({"display": "none"});
//     $('.field-teacher2').css({"display": "none"});
//     try {
//         if ($('[id="id_classroomscience_set-0-science"]')[0].value && !$('[id="id_classroomscience_set-0-teacher2"]')[0].value) {
//             change($('[id="id_classroomscience_set-0-science"]')[0].value);
//         }
//         console.log("success");
//     } catch(error) {
//         console.log(error);
//     }
// });

// document.addEventListener("change", (event) => {
//     let id = event.srcElement.id;
//     let value = event.target.value;
//     if (id === "id_classroomscience_set-0-science" && value) {
//         change(value);
//     }
//     console.log(event);
// });

// function change(value) {
//     console.log(value);
//     let url = "/class/science/is/group/?id=" + value;
//     $.ajax({
//         url: url,
//         success: function (data) {
//             if (data.is_group === true) {
//                 $('.column-teacher2').css({"display": "block"});
//                 $('.field-teacher2').css({"display": "block"});
//                 $('#id_classroomscience_set-0-teacher2').css({"display": "block"});
//             } else {
//                 $('.column-teacher2').css({"display": "none"});
//                 $('.field-teacher2').css({"display": "none"});
//                 $('#id_classroomscience_set-0-teacher2').css({"display": "none"});
//             }
//         },
//         error: function (xhr, status, error) {
//             console.log("error", error);
//         }
//     });
//     console.log(value);
//     if (value === 1 || value === "1") {
//         console.log("matmatika");
//     } else {
//         console.log("english");
//     }
// }


$(document).ready(function() {
    // page reload and add page
    // $('.column-teacher2').css({"display": "none"});
    // $('.field-teacher2').css({"display": "none"});
    for (let i=0; i<30; i++) {
        try {
            if ($(`[id="id_classroomscience_set-${i}-science"]`)[0].value && !$(`[id="id_classroomscience_set-${i}-teacher2"]`)[0].value) {
                change($(`[id="id_classroomscience_set-${i}-science"]`)[0].value);
            }
        } catch(error) {
            console.log(error);
        }
    }
    console.log("success");
});

document.addEventListener("change", (event) => {
    let id = event.srcElement.id;
    let value = event.target.value;
    if (id.indexOf("id_classroomscience_set") !== -1 && value && id.indexOf("science") !== -1) {
        let id_number = id.split("-")[1];
        change(value, id_number);
    }
    console.log(event);
});

function change(value, id) {
    console.log(id);
    let url = "/class/science/is/group/?id=" + value;
    $.ajax({
        url: url,
        success: function (data) {
            if (data.is_group === true) {
                // $('.column-teacher2').css({"display": "block"});
                // $('.field-teacher2').css({"display": "block"});
                $(`#id_classroomscience_set-${id}-teacher2`).css({"display": "block"});
            } else {
                // $('.column-teacher2').css({"display": "none"});
                // $('.field-teacher2').css({"display": "none"});
                $(`#id_classroomscience_set-${id}-teacher2`).css({"display": "none"});
            }
        }
    });
    console.log(value);
    if (value === 1 || value === "1") {
        console.log("matmatika");
    } else {
        console.log("english");
    }
}