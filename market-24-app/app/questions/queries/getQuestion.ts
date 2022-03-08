import { resolver, NotFoundError } from "blitz"
import db from "db"
import { z } from "zod"

const GetQuestion = z.object({
  // This accepts type of undefined, but is required at runtime
  id: z.number().optional().refine(Boolean, "Required"),
})

export default resolver.pipe(resolver.zod(GetQuestion), resolver.authorize(), async ({ id }) => {
  // TODO: in multi-tenant app, you must add validation to ensure correct tenant
  const question = await db.question.findFirst({ where: { id } })

  if (!question) throw new NotFoundError()

  return question
})
