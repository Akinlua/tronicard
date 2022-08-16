


// $(document).ready(function(){
//     $("#load-btn").on('click',function(e){
//         e.preventDefault()
//         console.log('click')
//         var _currentResult=$(".comment-box").length
//         // var _currentResult=2
//         console.log(_currentResult)
//         blog_id=$(".blogid").val()
//         console.log(blog_id)
//         $.ajax({
//             url:'{% url "loadmore" %}',
//             type:'post',
//             data:{
//                 'offset':_currentResult,
//                 'blog_id':blog_id,
//                 'csrfmiddlewaretoken':'{{csrf_token}}',
//             },
//             dataType:'json',
//             beforeSend:function(){
//                 $("#load-btn").addClass('disabled').text('loading')
//             },
//             success:function(res){
//                 console.log(res)
//                 // var _html=''
//                 // var json_data=$.parseJSON(res.comment)
//                 // $.each(json_data, function(index,data){
//                 //     _html+=''

//                 // })
//                 // $(".container-comments").append(_html)
//                 // var _count_total=$(".comment-box").length
//                 // console.log(_count_total)
//                 // if(_count_total>=res.totalResult){
//                 //       $("#load-btn").remove()
//                 // }else{
//                 //     $("#load-btn").removeClass('disabled').text('Load more')
//                 // }
                

//             }
//         })

//     })
// })

