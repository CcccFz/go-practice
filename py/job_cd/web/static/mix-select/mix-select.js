CONDITION = {sort: [], benefit: [], salary: []};

$(function() {

	$('.mix-select tr td').click(function() {
		var $tr = $(this).parent();
		var isChoose = $(this).children().eq(0).hasClass('active');
		var key = $(this).parents('table').children().eq(0).attr('class');
		var cond = CONDITION[key];
		var value = $(this).children().eq(0).text();

		if ($(this).index() === 0) {
			cond = [];
			$(this).children().eq(0).addClass('active');
			$.each($(this).siblings(), function (i, item) {
				$(item).children().eq(0).removeClass('active');
			});
		} else {
			$(this).siblings().eq(0).children().eq(0).removeClass('active');

			if (isChoose) {
				$(this).children().eq(0).removeClass('active');
				cond = $.grep(cond, function(item) {
 					return item !== value;
				});
			} else {
				$(this).children().eq(0).addClass('active');
				cond.push(value);
			}

			if ($tr.find('.active').length === 0) {
				$tr.find('a').eq(0).addClass('active');
			}
		}

		CONDITION[key] = cond;
		SendCond(CONDITION);
	});

	$('.mix-select .mix-select-sort a').click(function() {
		var $div = $(this).parent();
		var isChooseUp = $(this).hasClass('active-up');
		var isChooseDown = $(this).hasClass('active-down');
		var cond = CONDITION['sort'];
		var value = $(this).text();

		if ($(this).index() === 0) {
			cond = [];
			$(this).siblings().removeClass('active-up');
			$(this).siblings().removeClass('active-down');
			$(this).addClass('active');
		} else {
			$(this).siblings().eq(0).removeClass('active');

			if (isChooseDown) {
				$(this).attr('class', 'active-up');
				$.each(cond, function (i, item) {
					if (item === value + '-down') {
						cond[i] = value + '-up';
					}
                });
			} else if (isChooseUp) {
				$(this).removeClass('active-up');
				cond = $.grep(cond, function(item) {
					return item !== value + '-up';
				});
			} else {
				$(this).attr('class', 'active-down');
				cond.push(value + '-down');
			}

			if ($div.children('.active-up').length === 0 && $div.children('.active-down').length === 0) {
				$div.children('a').eq(0).addClass('active');
			}
		}

		CONDITION['sort'] = cond;
		SendCond(CONDITION);
	});

});



