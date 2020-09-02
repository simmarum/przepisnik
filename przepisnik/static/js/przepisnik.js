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

function SendRateProduct(rate, page_ptr_id) {
    console.log("@", rate, page_ptr_id);
    tmp_span = document.createElement('div');
    tmp_span.innerHTML = gettext("You rated the product with a %1 grade.").replace('%1', rate);
    tmp_rate = document.getElementById("rate_star");
    tmp_rate.replaceWith(tmp_span);
    // TODO log it to database
    // TODO update actual rate in product
}