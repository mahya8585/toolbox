import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
})

export default {
  /** 顧客情報を取得 */
  getCustomer(customerId) {
    return api.get(`/customers/${customerId}`).then(r => r.data)
  },

  /** 推奨商品一覧（顧客情報+レコメンド）を取得 */
  getRecommendations(customerId) {
    return api.get(`/recommendations/${customerId}`).then(r => r.data)
  },

  /** 類似顧客の投資行動を取得 */
  getSimilarCustomers(customerId) {
    return api.get(`/customers/${customerId}/similar`).then(r => r.data)
  },

  /** 市場トレンドを取得 */
  getMarketTrends() {
    return api.get('/market/trends').then(r => r.data)
  },
}
