var email_regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/
var csrf_token = $("#csrf").val();


$('#student').on('click', function(){
    $('#user_type').val('student');
});
$('#teacher').on('click', function(){
    $('#user_type').val('teacher');
});

$('#panel2_next_btn').on('click', function(){
    var first_name = $("#first_name").val();
    var last_name = $("#last_name").val();
    var email = $("#signup_email").val();
    
    if(first_name == ''){
        $('#f_name_error').html('Please enter first name');
        return false
    }else{
        $('#f_name_error').html('');
    }

    if(last_name == ''){
        $('#l_name_error').html('Please enter last name');
        return false
    }else{
        $('#l_name_error').html('');
    }
    
    if(email == '' || !email_regex.test(email)){
        $('#signup_email_error').html('Please enter valid email');
        return false
    }else{
        $('#signup_email_error').html('');
    }

    $.ajax({
        url : "/email-checking/",
        data : {'email':email},
        success : function(data){
            if(data['valid']){
                $('#signup_email_error').html('');
                $("#step-dot-3").click();
            }else{
                $('#signup_email_error').html('Email already exists');
            }
        }
    });
});

$("#panel4_next_btn").on('click', function(){
    var first_name = $("#first_name").val();
    var last_name = $("#last_name").val();
    var email = $("#signup_email").val();
    var password = $("#password").val();
    var repeat_password = $("#repeat_password").val();
    var phone_number = $("#phone_number").val();
    var user_type = $('#user_type').val();
    
    if(password.length < 8){
        $('#password_error').html('Password must be length of 8');
        return false
    }else{
        $('#password_error').html('');
    }

    if(repeat_password == '' || password != repeat_password){
        $('#r_password_error').html('Password not match');
        return false
    }else{
        $('#r_password_error').html('');
    }

    if(phone_number.length != 10){
        $('#phone_number_error').html('Please enter valid phone number');
        return false
    }else{
        $('#phone_number_error').html('');
    }

    $.ajax({
        type : "POST",
        url : "/signup/",
        data : {
            'csrfmiddlewaretoken' : csrf_token,
            'first_name'          : first_name,
            'last_name'           : last_name,
            'email'               : email,
            'password'            : password,
            'phone_number'        : phone_number,
            'user_type'           : user_type,
        },
        success : function(data){
            if(data['success']){
                $('#step-dot-5').click();
            }
        },
        error : function(data){
            console.log(data);
        }
    });
});

$(".login_btn").on('click', function(){
    var email = $("#login_email").val();
    var password = $("#login_password").val();
        
    if(email == '' || !email_regex.test(email)){
        $("#login_email_error").html("Please enter valid email");
        return false
    }else{
        $("#login_email_error").html("");
    }
        
    if(password == ''){
        $("#login_password_error").html("Please enter password");
        return false
    }else{
        $("#login_password_error").html("");
    }

    $.ajax({
        type : 'POST',
        url : "/login/",
        data : {
            'csrfmiddlewaretoken' : csrf_token,
            'email' : email,
            'password' : password,
        },
        success : function(data){
            if(data['email_error']){
                $("#login_email_error").html("Email not registered");
                return false
            }
            if(data['password_error']){
                $("#login_password_error").html("Wrong password");
                return false
            }
            if(data['success']){
                location.reload();
            }
        },
        error : function(data){
            location.reload();
        }
    });
});

$("#logout_btn").on('click', function(){
    $.ajax({
        url : "/logout/",
        success : function(data){
            location.reload();
        },
        error : function(data){
            location.reload();
        }
    });
});