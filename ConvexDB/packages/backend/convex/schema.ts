import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
   enoded_msg: defineTable({
      userId: v.string(),
      title: v.string(),
      content: v.string(),
   }),

 notes: defineTable({
    userId: v.string(),
    title: v.string(),
    content: v.string(),
 }),

 culprits: defineTable({
    userId: v.string(),
    title: v.string(),
    content: v.string()
 }),


 messages: defineTable({
   description: v.string(),

}),
});
