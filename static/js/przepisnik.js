function CountDownTimer(duration, granularity, id_of_span) {
    this.duration = duration;
    this.granularity = granularity || 1000;
    this.id_of_span = id_of_span;
    this.tickFtns = [];
    this.running = false;
}

CountDownTimer.prototype.start = function () {
    if (this.running) {
        return;
    }
    this.running = true;
    var start = Date.now(),
        that = this,
        diff, obj;

    (function timer() {
        diff = that.duration - (((Date.now() - start) / 1000) | 0);

        if (diff > 0) {
            setTimeout(timer, that.granularity);
        } else {
            diff = 0;
            that.running = false;
        }

        obj = CountDownTimer.parse(diff);
        that.tickFtns.forEach(function (ftn) {
            ftn.call(this, obj.minutes, obj.seconds, this.id_of_span);
        }, that);
    }());
};

CountDownTimer.prototype.onTick = function (ftn) {
    if (typeof ftn === 'function') {
        this.tickFtns.push(ftn);
    }
    return this;
};

CountDownTimer.prototype.expired = function () {
    return !this.running;
};

CountDownTimer.parse = function (seconds) {
    return {
        'minutes': (seconds / 60) | 0,
        'seconds': (seconds % 60) | 0
    };
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function SendRateProduct(rate, page_ptr_id) {
    tmp_span = document.createElement('div');
    tmp_span.innerHTML = gettext("You rated the product with a %1 grade.").replace('%1', rate);
    tmp_rate = document.getElementById("rate_star");
    tmp_rate.replaceWith(tmp_span);

    var csrftoken = getCookie('csrftoken');

    const url_rate = "/rate/";
    const data_rate = {
        'page_ptr_id': page_ptr_id,
        'rate': rate,
        'csrfmiddlewaretoken': csrftoken
    };
    $.post(url_rate, data_rate, function (data, status) {
    })
}