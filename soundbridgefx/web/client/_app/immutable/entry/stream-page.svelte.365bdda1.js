import{S as w,i as p,s as g,ad as v,k as u,l as m,m as _,h as d,ae as E,n as l,b,a5 as k,C as q,Z as c}from"../chunks/index.72b3cb36.js";function z(a){let i,e,h,r,n,o,f;return v(a[2]),{c(){i=u("div"),e=u("iframe"),this.h()},l(t){i=m(t,"DIV",{});var s=_(i);e=m(s,"IFRAME",{src:!0,height:!0,width:!0,title:!0}),_(e).forEach(d),s.forEach(d),this.h()},h(){E(e.src,h="http://localhost:6207/stream_raw")||l(e,"src",h),l(e,"height",r=a[1]-a[1]/10),l(e,"width",n=a[0]-a[0]/200),l(e,"title","stream iframe")},m(t,s){b(t,i,s),k(i,e),o||(f=q(window,"resize",a[2]),o=!0)},p(t,[s]){s&2&&r!==(r=t[1]-t[1]/10)&&l(e,"height",r),s&1&&n!==(n=t[0]-t[0]/200)&&l(e,"width",n)},i:c,o:c,d(t){t&&d(i),o=!1,f()}}}function C(a,i,e){let h=0,r=0;function n(){e(0,h=window.innerWidth),e(1,r=window.innerHeight)}return[h,r,n]}class I extends w{constructor(i){super(),p(this,i,C,z,g,{})}}export{I as default};
