function g(){}function G(t,e){for(const n in e)t[n]=e[n];return t}function I(t){return!!t&&(typeof t=="object"||typeof t=="function")&&typeof t.then=="function"}function B(t){return t()}function P(){return Object.create(null)}function x(t){t.forEach(B)}function S(t){return typeof t=="function"}function dt(t,e){return t!=t?e==e:t!==e||t&&typeof t=="object"||typeof t=="function"}let $;function ht(t,e){return $||($=document.createElement("a")),$.href=e,t===$.href}function J(t){return Object.keys(t).length===0}function K(t,...e){if(t==null)return g;const n=t.subscribe(...e);return n.unsubscribe?()=>n.unsubscribe():n}function mt(t,e,n){t.$$.on_destroy.push(K(e,n))}function pt(t,e,n,r){if(t){const c=H(t,e,n,r);return t[0](c)}}function H(t,e,n,r){return t[1]&&r?G(n.ctx.slice(),t[1](r(e))):n.ctx}function yt(t,e,n,r){if(t[2]&&r){const c=t[2](r(n));if(e.dirty===void 0)return c;if(typeof c=="object"){const u=[],s=Math.max(e.dirty.length,c.length);for(let l=0;l<s;l+=1)u[l]=e.dirty[l]|c[l];return u}return e.dirty|c}return e.dirty}function gt(t,e,n,r,c,u){if(c){const s=H(e,n,r,u);t.p(s,c)}}function bt(t){if(t.ctx.length>32){const e=[],n=t.ctx.length/32;for(let r=0;r<n;r++)e[r]=-1;return e}return-1}function xt(t){const e={};for(const n in t)n[0]!=="$"&&(e[n]=t[n]);return e}function $t(t,e){const n={};e=new Set(e);for(const r in t)!e.has(r)&&r[0]!=="$"&&(n[r]=t[r]);return n}function wt(t){const e={};for(const n in t)e[n]=!0;return e}function kt(t,e,n){return t.set(n),e}function Et(t){return t&&S(t.destroy)?t.destroy:g}let E=!1;function Q(){E=!0}function U(){E=!1}function V(t,e,n,r){for(;t<e;){const c=t+(e-t>>1);n(c)<=r?t=c+1:e=c}return t}function X(t){if(t.hydrate_init)return;t.hydrate_init=!0;let e=t.childNodes;if(t.nodeName==="HEAD"){const i=[];for(let o=0;o<e.length;o++){const f=e[o];f.claim_order!==void 0&&i.push(f)}e=i}const n=new Int32Array(e.length+1),r=new Int32Array(e.length);n[0]=-1;let c=0;for(let i=0;i<e.length;i++){const o=e[i].claim_order,f=(c>0&&e[n[c]].claim_order<=o?c+1:V(1,c,d=>e[n[d]].claim_order,o))-1;r[i]=n[f]+1;const a=f+1;n[a]=i,c=Math.max(a,c)}const u=[],s=[];let l=e.length-1;for(let i=n[c]+1;i!=0;i=r[i-1]){for(u.push(e[i-1]);l>=i;l--)s.push(e[l]);l--}for(;l>=0;l--)s.push(e[l]);u.reverse(),s.sort((i,o)=>i.claim_order-o.claim_order);for(let i=0,o=0;i<s.length;i++){for(;o<u.length&&s[i].claim_order>=u[o].claim_order;)o++;const f=o<u.length?u[o]:null;t.insertBefore(s[i],f)}}function Y(t,e){if(E){for(X(t),(t.actual_end_child===void 0||t.actual_end_child!==null&&t.actual_end_child.parentNode!==t)&&(t.actual_end_child=t.firstChild);t.actual_end_child!==null&&t.actual_end_child.claim_order===void 0;)t.actual_end_child=t.actual_end_child.nextSibling;e!==t.actual_end_child?(e.claim_order!==void 0||e.parentNode!==t)&&t.insertBefore(e,t.actual_end_child):t.actual_end_child=e.nextSibling}else(e.parentNode!==t||e.nextSibling!==null)&&t.appendChild(e)}function vt(t,e,n){E&&!n?Y(t,e):(e.parentNode!==t||e.nextSibling!=n)&&t.insertBefore(e,n||null)}function Z(t){t.parentNode&&t.parentNode.removeChild(t)}function Nt(t,e){for(let n=0;n<t.length;n+=1)t[n]&&t[n].d(e)}function tt(t){return document.createElement(t)}function et(t){return document.createElementNS("http://www.w3.org/2000/svg",t)}function T(t){return document.createTextNode(t)}function jt(){return T(" ")}function At(){return T("")}function St(t,e,n,r){return t.addEventListener(e,n,r),()=>t.removeEventListener(e,n,r)}function Tt(t){return function(e){return e.preventDefault(),t.call(this,e)}}function Ct(t){return function(e){return e.stopPropagation(),t.call(this,e)}}function C(t,e,n){n==null?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}function Dt(t,e){const n=Object.getOwnPropertyDescriptors(t.__proto__);for(const r in e)e[r]==null?t.removeAttribute(r):r==="style"?t.style.cssText=e[r]:r==="__value"?t.value=t[r]=e[r]:n[r]&&n[r].set?t[r]=e[r]:C(t,r,e[r])}function Ot(t,e){for(const n in e)C(t,n,e[n])}function Mt(t,e){Object.keys(e).forEach(n=>{nt(t,n,e[n])})}function nt(t,e,n){e in t?t[e]=typeof t[e]=="boolean"&&n===""?!0:n:C(t,e,n)}function rt(t){return Array.from(t.childNodes)}function ct(t){t.claim_info===void 0&&(t.claim_info={last_index:0,total_claimed:0})}function L(t,e,n,r,c=!1){ct(t);const u=(()=>{for(let s=t.claim_info.last_index;s<t.length;s++){const l=t[s];if(e(l)){const i=n(l);return i===void 0?t.splice(s,1):t[s]=i,c||(t.claim_info.last_index=s),l}}for(let s=t.claim_info.last_index-1;s>=0;s--){const l=t[s];if(e(l)){const i=n(l);return i===void 0?t.splice(s,1):t[s]=i,c?i===void 0&&t.claim_info.last_index--:t.claim_info.last_index=s,l}}return r()})();return u.claim_order=t.claim_info.total_claimed,t.claim_info.total_claimed+=1,u}function z(t,e,n,r){return L(t,c=>c.nodeName===e,c=>{const u=[];for(let s=0;s<c.attributes.length;s++){const l=c.attributes[s];n[l.name]||u.push(l.name)}u.forEach(s=>c.removeAttribute(s))},()=>r(e))}function Pt(t,e,n){return z(t,e,n,tt)}function qt(t,e,n){return z(t,e,n,et)}function it(t,e){return L(t,n=>n.nodeType===3,n=>{const r=""+e;if(n.data.startsWith(r)){if(n.data.length!==r.length)return n.splitText(r.length)}else n.data=r},()=>T(e),!0)}function Bt(t){return it(t," ")}function Ht(t,e){e=""+e,t.wholeText!==e&&(t.data=e)}function Lt(t,e,n,r){n===null?t.style.removeProperty(e):t.style.setProperty(e,n,r?"important":"")}function zt(t,e){const n=[];let r=0;for(const c of e.childNodes)if(c.nodeType===8){const u=c.textContent.trim();u===`HEAD_${t}_END`?(r-=1,n.push(c)):u===`HEAD_${t}_START`&&(r+=1,n.push(c))}else r>0&&n.push(c);return n}function Ft(t,e){return new t(e)}let b;function _(t){b=t}function y(){if(!b)throw new Error("Function called outside component initialization");return b}function Rt(t){y().$$.on_mount.push(t)}function Wt(t){y().$$.after_update.push(t)}function Gt(t){y().$$.on_destroy.push(t)}function It(t,e){return y().$$.context.set(t,e),e}function Jt(t){return y().$$.context.get(t)}function Kt(t,e){const n=t.$$.callbacks[e.type];n&&n.slice().forEach(r=>r.call(this,e))}const p=[],q=[],w=[],N=[],F=Promise.resolve();let j=!1;function R(){j||(j=!0,F.then(D))}function Qt(){return R(),F}function A(t){w.push(t)}function Ut(t){N.push(t)}const v=new Set;let m=0;function D(){if(m!==0)return;const t=b;do{try{for(;m<p.length;){const e=p[m];m++,_(e),st(e.$$)}}catch(e){throw p.length=0,m=0,e}for(_(null),p.length=0,m=0;q.length;)q.pop()();for(let e=0;e<w.length;e+=1){const n=w[e];v.has(n)||(v.add(n),n())}w.length=0}while(p.length);for(;N.length;)N.pop()();j=!1,v.clear(),_(t)}function st(t){if(t.fragment!==null){t.update(),x(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(A)}}const k=new Set;let h;function ut(){h={r:0,c:[],p:h}}function ot(){h.r||x(h.c),h=h.p}function W(t,e){t&&t.i&&(k.delete(t),t.i(e))}function lt(t,e,n,r){if(t&&t.o){if(k.has(t))return;k.add(t),h.c.push(()=>{k.delete(t),r&&(n&&t.d(1),r())}),t.o(e)}else r&&r()}function Vt(t,e){const n=e.token={};function r(c,u,s,l){if(e.token!==n)return;e.resolved=l;let i=e.ctx;s!==void 0&&(i=i.slice(),i[s]=l);const o=c&&(e.current=c)(i);let f=!1;e.block&&(e.blocks?e.blocks.forEach((a,d)=>{d!==u&&a&&(ut(),lt(a,1,1,()=>{e.blocks[d]===a&&(e.blocks[d]=null)}),ot())}):e.block.d(1),o.c(),W(o,1),o.m(e.mount(),e.anchor),f=!0),e.block=o,e.blocks&&(e.blocks[u]=o),f&&D()}if(I(t)){const c=y();if(t.then(u=>{_(c),r(e.then,1,e.value,u),_(null)},u=>{if(_(c),r(e.catch,2,e.error,u),_(null),!e.hasCatch)throw u}),e.current!==e.pending)return r(e.pending,0),!0}else{if(e.current!==e.then)return r(e.then,1,e.value,t),!0;e.resolved=t}}function Xt(t,e,n){const r=e.slice(),{resolved:c}=t;t.current===t.then&&(r[t.value]=c),t.current===t.catch&&(r[t.error]=c),t.block.p(r,n)}const Yt=typeof window<"u"?window:typeof globalThis<"u"?globalThis:global;function Zt(t,e){const n={},r={},c={$$scope:1};let u=t.length;for(;u--;){const s=t[u],l=e[u];if(l){for(const i in s)i in l||(r[i]=1);for(const i in l)c[i]||(n[i]=l[i],c[i]=1);t[u]=l}else for(const i in s)c[i]=1}for(const s in r)s in n||(n[s]=void 0);return n}function te(t){return typeof t=="object"&&t!==null?t:{}}function ee(t,e,n){const r=t.$$.props[e];r!==void 0&&(t.$$.bound[r]=n,n(t.$$.ctx[r]))}function ne(t){t&&t.c()}function re(t,e){t&&t.l(e)}function at(t,e,n,r){const{fragment:c,after_update:u}=t.$$;c&&c.m(e,n),r||A(()=>{const s=t.$$.on_mount.map(B).filter(S);t.$$.on_destroy?t.$$.on_destroy.push(...s):x(s),t.$$.on_mount=[]}),u.forEach(A)}function ft(t,e){const n=t.$$;n.fragment!==null&&(x(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}function _t(t,e){t.$$.dirty[0]===-1&&(p.push(t),R(),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function ce(t,e,n,r,c,u,s,l=[-1]){const i=b;_(t);const o=t.$$={fragment:null,ctx:[],props:u,update:g,not_equal:c,bound:P(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(e.context||(i?i.$$.context:[])),callbacks:P(),dirty:l,skip_bound:!1,root:e.target||i.$$.root};s&&s(o.root);let f=!1;if(o.ctx=n?n(t,e.props||{},(a,d,...O)=>{const M=O.length?O[0]:d;return o.ctx&&c(o.ctx[a],o.ctx[a]=M)&&(!o.skip_bound&&o.bound[a]&&o.bound[a](M),f&&_t(t,a)),d}):[],o.update(),f=!0,x(o.before_update),o.fragment=r?r(o.ctx):!1,e.target){if(e.hydrate){Q();const a=rt(e.target);o.fragment&&o.fragment.l(a),a.forEach(Z)}else o.fragment&&o.fragment.c();e.intro&&W(t.$$.fragment),at(t,e.target,e.anchor,e.customElement),U(),D()}_(i)}class ie{$destroy(){ft(this,1),this.$destroy=g}$on(e,n){if(!S(n))return g;const r=this.$$.callbacks[e]||(this.$$.callbacks[e]=[]);return r.push(n),()=>{const c=r.indexOf(n);c!==-1&&r.splice(c,1)}}$set(e){this.$$set&&!J(e)&&(this.$$.skip_bound=!0,this.$$set(e),this.$$.skip_bound=!1)}}export{et as $,Qt as A,g as B,St as C,Kt as D,Tt as E,Ct as F,pt as G,G as H,Dt as I,Et as J,gt as K,bt as L,yt as M,Zt as N,S as O,x as P,$t as Q,y as R,ie as S,xt as T,Yt as U,q as V,te as W,Jt as X,It as Y,Gt as Z,K as _,jt as a,qt as a0,Ot as a1,ee as a2,Ut as a3,zt as a4,Y as a5,Mt as a6,mt as a7,kt as a8,wt as a9,Vt as aa,Xt as ab,Nt as ac,A as ad,ht as ae,vt as b,Bt as c,ot as d,At as e,W as f,ut as g,Z as h,ce as i,Wt as j,tt as k,Pt as l,rt as m,C as n,Rt as o,Lt as p,T as q,it as r,dt as s,lt as t,Ht as u,Ft as v,ne as w,re as x,at as y,ft as z};
